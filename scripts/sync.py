import os
import json
import time
import base64
import requests
from slugify import slugify

# ── Config ──────────────────────────────────────────────────────────────────
SESSION_COOKIE = os.environ["LEETCODE_SESSION"]
OUTPUT_DIR = "problems"
PROGRESS_FILE = ".sync_state.json"
GRAPHQL_URL = "https://leetcode.com/graphql"
PAGE_SIZE = 20
RATE_DELAY = 1.5

# ── Extract CSRF token from the session JWT payload ─────────────────────────
def get_csrf_token():
    try:
        parts = SESSION_COOKIE.split(".")
        if len(parts) >= 2:
            payload = parts[1]
            payload += "=" * (4 - len(payload) % 4)
            decoded = json.loads(base64.urlsafe_b64decode(payload))
            csrf = decoded.get("csrfToken") or decoded.get("csrf_token")
            if csrf:
                return csrf
    except Exception as e:
        print(f"  ⚠️  JWT decode failed: {e}")
    return "leetcode-sync-csrf-token"

CSRF_TOKEN = get_csrf_token()
print(f"  🔑 Using CSRF token: {CSRF_TOKEN[:12]}...")

HEADERS = {
    "Cookie": f"LEETCODE_SESSION={SESSION_COOKIE}; csrftoken={CSRF_TOKEN}",
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "x-csrftoken": CSRF_TOKEN,
    "Origin": "https://leetcode.com",
}

# ── Language → file extension map ───────────────────────────────────────────
LANG_EXT = {
    "python": "py", "python3": "py", "cpp": "cpp", "c": "c",
    "java": "java", "javascript": "js", "typescript": "ts",
    "golang": "go", "rust": "rs", "kotlin": "kt", "swift": "swift",
    "scala": "scala", "ruby": "rb", "php": "php", "csharp": "cs",
    "mysql": "sql", "bash": "sh",
}

DIFFICULTY_EMOJI = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}

# ── State helpers ────────────────────────────────────────────────────────────
def load_state():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {"synced_ids": [], "first_run": True}

def save_state(state):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(state, f, indent=2)

# ── GraphQL helper ───────────────────────────────────────────────────────────
def graphql(query, variables=None):
    resp = requests.post(
        GRAPHQL_URL,
        headers=HEADERS,
        json={"query": query, "variables": variables or {}},
        timeout=20,
    )
    if not resp.ok:
        print(f"  ❌ GraphQL error {resp.status_code}: {resp.text[:300]}")
    resp.raise_for_status()
    return resp.json()

# ── Get current username ─────────────────────────────────────────────────────
def get_username():
    query = """
    query globalData {
      userStatus { username }
    }
    """
    data = graphql(query)
    username = data["data"]["userStatus"]["username"]
    print(f"  👤 Logged in as: {username}")
    return username

# ── Fetch ALL accepted submissions via pagination ────────────────────────────
def get_all_accepted_submissions(username):
    """
    Paginate through ALL submissions, filter to Accepted only,
    and keep the most recent accepted submission per problem.
    """
    query = """
    query submissionList($offset: Int!, $limit: Int!) {
      submissionList(offset: $offset, limit: $limit) {
        lastKey
        hasNext
        submissions {
          id
          titleSlug
          lang
          statusDisplay
          timestamp
        }
      }
    }
    """
    accepted = {}   # slug → most recent accepted submission
    offset = 0
    page = 1

    print("  📄 Paginating through full submission history...")
    while True:
        print(f"     page {page} (offset {offset})...")
        data = graphql(query, {"offset": offset, "limit": PAGE_SIZE})
        result = data["data"]["submissionList"]
        subs = result["submissions"]

        for sub in subs:
            if sub["statusDisplay"] == "Accepted":
                slug = sub["titleSlug"]
                # submissions are newest-first, so first seen = most recent
                if slug not in accepted:
                    accepted[slug] = sub

        if not result["hasNext"] or not subs:
            break

        offset += PAGE_SIZE
        page += 1
        time.sleep(RATE_DELAY)

    all_subs = list(accepted.values())
    print(f"  📊 Found {len(all_subs)} unique solved problems in history")
    return all_subs

# ── Fetch recent accepted submissions (normal runs) ──────────────────────────
def get_recent_accepted_submissions(username, limit=20):
    query = """
    query recentAcSubmissions($username: String!, $limit: Int!) {
      recentAcSubmissionList(username: $username, limit: $limit) {
        id
        titleSlug
        lang
        timestamp
      }
    }
    """
    data = graphql(query, {"username": username, "limit": limit})
    return data["data"]["recentAcSubmissionList"]

# ── Fetch submission code ────────────────────────────────────────────────────
def get_submission_detail(submission_id):
    query = """
    query submissionDetails($submissionId: Int!) {
      submissionDetails(submissionId: $submissionId) {
        code
        lang { name }
      }
    }
    """
    data = graphql(query, {"submissionId": int(submission_id)})
    return data["data"]["submissionDetails"]

# ── Fetch problem details ────────────────────────────────────────────────────
def get_problem_details(title_slug):
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionFrontendId
        title
        titleSlug
        difficulty
        content
        topicTags { name }
        hints
      }
    }
    """
    data = graphql(query, {"titleSlug": title_slug})
    return data["data"]["question"]

# ── HTML → Markdown ──────────────────────────────────────────────────────────
def html_to_markdown(html: str) -> str:
    import re
    html = re.sub(r"<pre>(.*?)</pre>", lambda m: "\n```\n" + m.group(1).strip() + "\n```\n", html, flags=re.DOTALL)
    html = re.sub(r"<code>(.*?)</code>", r"`\1`", html, flags=re.DOTALL)
    html = re.sub(r"<strong>(.*?)</strong>", r"**\1**", html, flags=re.DOTALL)
    html = re.sub(r"<em>(.*?)</em>", r"*\1*", html, flags=re.DOTALL)
    html = re.sub(r"<li>(.*?)</li>", r"- \1", html, flags=re.DOTALL)
    html = re.sub(r"<[^>]+>", "", html)
    html = html.replace("&nbsp;", " ").replace("&lt;", "<").replace("&gt;", ">") \
               .replace("&amp;", "&").replace("&#39;", "'").replace("&quot;", '"')
    return html.strip()

# ── Build README.md ──────────────────────────────────────────────────────────
def build_readme(problem, lang, submission_id):
    num   = problem["questionFrontendId"].zfill(4)
    title = problem["title"]
    diff  = problem["difficulty"]
    tags  = [t["name"] for t in problem["topicTags"]]
    desc  = html_to_markdown(problem["content"] or "")
    hints = problem.get("hints") or []
    ext   = LANG_EXT.get(lang, lang)
    emoji = DIFFICULTY_EMOJI.get(diff, "⚪")
    tag_badges = " ".join(f"`{t}`" for t in tags)

    hints_section = ""
    if hints:
        hints_md = "\n".join(f"{i+1}. {h}" for i, h in enumerate(hints))
        hints_section = f"\n## 💡 Hints\n\n<details>\n<summary>Show hints</summary>\n\n{hints_md}\n\n</details>\n"

    return f"""# {num}. {title}

{emoji} **Difficulty:** {diff} &nbsp;|&nbsp; 🏷️ **Topics:** {tag_badges}

---

## 📝 Problem Description

{desc}
{hints_section}
---

## ✅ My Solution

See [`solution.{ext}`](./solution.{ext})

---

*Synced automatically from [LeetCode](https://leetcode.com/problems/{problem['titleSlug']}/) · Submission ID: {submission_id}*
"""

# ── Write solution files ─────────────────────────────────────────────────────
def write_solution(problem, lang, code, submission_id):
    num    = problem["questionFrontendId"].zfill(4)
    slug   = problem["titleSlug"]
    ext    = LANG_EXT.get(lang, lang)
    folder = os.path.join(OUTPUT_DIR, f"{num}-{slug}")
    os.makedirs(folder, exist_ok=True)

    readme_path   = os.path.join(folder, "README.md")
    solution_path = os.path.join(folder, f"solution.{ext}")

    if not os.path.exists(readme_path):
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(build_readme(problem, lang, submission_id))

    with open(solution_path, "w", encoding="utf-8") as f:
        f.write(code)

    print(f"  ✅ {num}. {problem['title']} [{lang}]")

# ── Process a list of submissions ────────────────────────────────────────────
def process_submissions(submissions, synced_ids):
    new_count = 0
    for sub in submissions:
        sid = sub["id"]
        if sid in synced_ids:
            continue

        title_slug = sub["titleSlug"]
        lang       = sub["lang"]
        print(f"  → {title_slug}")

        try:
            detail = get_submission_detail(sid)
            if not detail:
                print(f"  ⚠️  Could not fetch code for {title_slug}, skipping")
                continue
            code    = detail["code"]
            problem = get_problem_details(title_slug)
            write_solution(problem, lang, code, sid)
            synced_ids.add(sid)
            new_count += 1
            time.sleep(RATE_DELAY)
        except Exception as e:
            print(f"  ⚠️  Skipped {title_slug}: {e}")

    return new_count

# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    state      = load_state()
    synced_ids = set(state["synced_ids"])
    first_run  = state.get("first_run", False)
    username   = get_username()

    if first_run:
        print("\n🚀 First run detected — performing full historical sync...")
        submissions = get_all_accepted_submissions(username)
    else:
        print("\n🔍 Fetching recent accepted submissions...")
        submissions = get_recent_accepted_submissions(username, limit=20)

    new_count = process_submissions(submissions, synced_ids)

    state["first_run"]  = False
    state["synced_ids"] = list(synced_ids)
    save_state(state)

    if new_count == 0:
        print("✨ Nothing new to sync.")
    else:
        print(f"\n🎉 Synced {new_count} new solution(s)!")

if __name__ == "__main__":
    main()
