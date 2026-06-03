import os
import json
import time
import requests
from slugify import slugify

# ── Config ──────────────────────────────────────────────────────────────────
SESSION_COOKIE = os.environ["LEETCODE_SESSION"]
OUTPUT_DIR = "problems"
PROGRESS_FILE = ".sync_state.json"
GRAPHQL_URL = "https://leetcode.com/graphql"

# ── Bootstrap: get a real csrftoken from LeetCode ───────────────────────────
def get_csrf_token():
    """Hit the LeetCode homepage to obtain a valid csrftoken cookie."""
    session = requests.Session()
    session.cookies.set("LEETCODE_SESSION", SESSION_COOKIE, domain="leetcode.com")
    resp = session.get(
        "https://leetcode.com/",
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=15,
    )
    csrf = session.cookies.get("csrftoken", domain="leetcode.com")
    if not csrf:
        # Fall back: parse from Set-Cookie header directly
        for c in resp.cookies:
            if c.name == "csrftoken":
                csrf = c.value
                break
    if not csrf:
        raise RuntimeError("Could not obtain csrftoken from LeetCode. Check your LEETCODE_SESSION secret.")
    return csrf

CSRF_TOKEN = get_csrf_token()

HEADERS = {
    "Cookie": f"LEETCODE_SESSION={SESSION_COOKIE}; csrftoken={CSRF_TOKEN}",
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com",
    "User-Agent": "Mozilla/5.0",
    "x-csrftoken": CSRF_TOKEN,
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
    )
    resp.raise_for_status()
    return resp.json()

# ── Fetch accepted submissions ───────────────────────────────────────────────
def get_accepted_submissions(limit=20, offset=0):
    query = """
    query recentAcSubmissions($limit: Int!, $offset: Int!) {
      submissionList(offset: $offset, limit: $limit, status: 10) {
        submissions {
          id
          titleSlug
          lang
          timestamp
          code
          statusDisplay
        }
      }
    }
    """
    data = graphql(query, {"limit": limit, "offset": offset})
    return data["data"]["submissionList"]["submissions"]

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
    """Very lightweight HTML → plain text for README."""
    import re
    html = re.sub(r"<pre>(.*?)</pre>", lambda m: "\n```\n" + m.group(1).strip() + "\n```\n", html, flags=re.DOTALL)
    html = re.sub(r"<code>(.*?)</code>", r"`\1`", html, flags=re.DOTALL)
    html = re.sub(r"<strong>(.*?)</strong>", r"**\1**", html, flags=re.DOTALL)
    html = re.sub(r"<em>(.*?)</em>", r"*\1*", html, flags=re.DOTALL)
    html = re.sub(r"<li>(.*?)</li>", r"- \1", html, flags=re.DOTALL)
    html = re.sub(r"<[^>]+>", "", html)
    html = html.replace("&nbsp;", " ").replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&").replace("&#39;", "'").replace("&quot;", '"')
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
def write_solution(problem, submission):
    num   = problem["questionFrontendId"].zfill(4)
    slug  = problem["titleSlug"]
    lang  = submission["lang"]
    code  = submission["code"]
    ext   = LANG_EXT.get(lang, lang)

    folder = os.path.join(OUTPUT_DIR, f"{num}-{slug}")
    os.makedirs(folder, exist_ok=True)

    readme_path  = os.path.join(folder, "README.md")
    solution_path = os.path.join(folder, f"solution.{ext}")

    # Only write README if it doesn't exist yet (problem desc doesn't change)
    if not os.path.exists(readme_path):
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(build_readme(problem, lang, submission["id"]))

    # Always write latest accepted solution
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
        print(f"  → Processing: {title_slug}")

        try:
            problem = get_problem_details(title_slug)
            write_solution(problem, sub)
            synced_ids.add(sid)
            new_count += 1
            time.sleep(1)  # be polite to LeetCode's API
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
