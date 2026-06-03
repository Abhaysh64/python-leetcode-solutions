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

# ── Extract CSRF token from the session JWT payload ─────────────────────────
def get_csrf_token():
    """
    LEETCODE_SESSION is a JWT (header.payload.sig).
    The payload contains a 'csrfToken' field we can decode without any library.
    """
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

    # Hard fallback — LeetCode sometimes accepts any consistent token
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

# ── Helpers ──────────────────────────────────────────────────────────────────
def load_state():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {"synced_ids": []}

def save_state(state):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(state, f, indent=2)

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

# ── Fetch accepted submissions ───────────────────────────────────────────────
def get_accepted_submissions(limit=20, offset=0):
    # Uses the correct query name that works for all users
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
    # First get the current username
    username = get_username()
    data = graphql(query, {"username": username, "limit": limit})
    return data["data"]["recentAcSubmissionList"]

def get_username():
    query = """
    query globalData {
      userStatus {
        username
      }
    }
    """
    data = graphql(query)
    username = data["data"]["userStatus"]["username"]
    print(f"  👤 Logged in as: {username}")
    return username

# ── Fetch submission code (separate query needed) ────────────────────────────
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

# ── Strip HTML from problem content ─────────────────────────────────────────
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

# ── Write files ──────────────────────────────────────────────────────────────
def write_solution(problem, lang, code, submission_id):
    num   = problem["questionFrontendId"].zfill(4)
    slug  = problem["titleSlug"]
    ext   = LANG_EXT.get(lang, lang)

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

# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    state = load_state()
    synced_ids = set(state["synced_ids"])

    print("🔍 Fetching recent accepted submissions...")
    submissions = get_accepted_submissions(limit=20)

    new_count = 0
    for sub in submissions:
        sid = sub["id"]
        if sid in synced_ids:
            continue

        title_slug = sub["titleSlug"]
        lang       = sub["lang"]
        print(f"  → Processing: {title_slug}")

        try:
            # Fetch code separately
            detail = get_submission_detail(sid)
            if not detail:
                print(f"  ⚠️  Could not fetch code for {title_slug}, skipping")
                continue
            code = detail["code"]

            problem = get_problem_details(title_slug)
            write_solution(problem, lang, code, sid)
            synced_ids.add(sid)
            new_count += 1
            time.sleep(1)
        except Exception as e:
            print(f"  ⚠️  Skipped {title_slug}: {e}")

    state["synced_ids"] = list(synced_ids)
    save_state(state)

    if new_count == 0:
        print("✨ Nothing new to sync.")
    else:
        print(f"\n🎉 Synced {new_count} new solution(s)!")

if __name__ == "__main__":
    main()
