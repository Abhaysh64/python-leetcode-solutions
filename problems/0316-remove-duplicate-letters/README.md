# 0316. Remove Duplicate Letters

🟡 **Difficulty:** Medium &nbsp;|&nbsp; 🏷️ **Topics:** `String` `Stack` `Greedy` `Monotonic Stack`

---

## 📝 Problem Description

Given a string `s`, remove duplicate letters so that every letter appears once and only once. You must make sure your result is **the smallest in lexicographical order** among all possible results.

 
Example 1:


```
**Input:** s = "bcabc"
**Output:** "abc"
```


Example 2:


```
**Input:** s = "cbacdcbc"
**Output:** "acdb"
```


 
**Constraints:**


	- `1 <= s.length <= 104`
	- `s` consists of lowercase English letters.


 
**Note:** This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

## 💡 Hints

<details>
<summary>Show hints</summary>

1. Greedily try to add one missing character. How to check if adding some character will not cause problems ? Use bit-masks to check whether you will be able to complete the sub-sequence if you add the character at some index i.

</details>

---

## ✅ My Solution

See [`solution.cpp`](./solution.cpp)

---

*Synced automatically from [LeetCode](https://leetcode.com/problems/remove-duplicate-letters/) · Submission ID: 1059809177*
