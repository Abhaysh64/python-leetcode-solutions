# 🧩 LeetCode Solutions

Auto-synced solutions to LeetCode problems, organized by problem number.

![Sync Status](https://github.com/Abhaysh64/python-leetcode-solutions/actions/workflows/sync.yml/badge.svg)

## 📁 Structure

```
problems/
├── 0001-two-sum/
│   ├── README.md       ← problem description, difficulty, tags, hints
│   └── solution.py     ← your accepted solution
├── 0002-add-two-numbers/
│   ├── README.md
│   └── solution.js
...
```

## ⚙️ How it works

1. A GitHub Action runs **every 6 hours**
2. It fetches your latest accepted submissions from LeetCode
3. For each new solution, it creates a folder with:
   - `README.md` — full problem description, difficulty, topic tags, and hints
   - `solution.<ext>` — your accepted code
4. Changes are committed and pushed automatically to the repository

## 🚀 Setup (one-time)

1. Fork or clone this repo
2. Go to **Settings → Secrets → Actions**
3. Add secret: `LEETCODE_SESSION` (copy from your browser cookies on leetcode.com)
4. Done! The workflow runs automatically every 12 hour.

> **Tip:** Don't log out of LeetCode explicitly — your session cookie will stay valid for months.
