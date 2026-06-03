# 1456. Maximum Number of Vowels in a Substring of Given Length

🟡 **Difficulty:** Medium &nbsp;|&nbsp; 🏷️ **Topics:** `String` `Sliding Window`

---

## 📝 Problem Description

Given a string `s` and an integer `k`, return *the maximum number of vowel letters in any substring of *`s`* with length *`k`.

**Vowel letters** in English are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

 
Example 1:


```
**Input:** s = "abciiidef", k = 3
**Output:** 3
**Explanation:** The substring "iii" contains 3 vowel letters.
```


Example 2:


```
**Input:** s = "aeiou", k = 2
**Output:** 2
**Explanation:** Any substring of length 2 contains 2 vowels.
```


Example 3:


```
**Input:** s = "leetcode", k = 3
**Output:** 2
**Explanation:** "lee", "eet" and "ode" contain 2 vowels.
```


 
**Constraints:**


	- `1 <= s.length <= 105`
	- `s` consists of lowercase English letters.
	- `1 <= k <= s.length`

## 💡 Hints

<details>
<summary>Show hints</summary>

1. Keep a window of size k and maintain the number of vowels in it.
2. Keep moving the window and update the number of vowels while moving. Answer is max number of vowels of any window.

</details>

---

## ✅ My Solution

See [`solution.cpp`](./solution.cpp)

---

*Synced automatically from [LeetCode](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) · Submission ID: 944728605*
