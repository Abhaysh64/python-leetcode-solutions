# 1980. Find Unique Binary String

🟡 **Difficulty:** Medium &nbsp;|&nbsp; 🏷️ **Topics:** `Array` `Hash Table` `String` `Backtracking`

---

## 📝 Problem Description

Given an array of strings `nums` containing `n` **unique** binary strings each of length `n`, return *a binary string of length *`n`* that **does not appear** in *`nums`*. If there are multiple answers, you may return **any** of them*.

 
Example 1:


```
**Input:** nums = ["01","10"]
**Output:** "11"
**Explanation:** "11" does not appear in nums. "00" would also be correct.
```


Example 2:


```
**Input:** nums = ["00","01"]
**Output:** "11"
**Explanation:** "11" does not appear in nums. "10" would also be correct.
```


Example 3:


```
**Input:** nums = ["111","011","001"]
**Output:** "101"
**Explanation:** "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
```


 
**Constraints:**


	- `n == nums.length`
	- `1 <= n <= 16`
	- `nums[i].length == n`
	- `nums[i] `is either `'0'` or `'1'`.
	- All the strings of `nums` are **unique**.

## 💡 Hints

<details>
<summary>Show hints</summary>

1. We can convert the given strings into base 10 integers.
2. Can we use recursion to generate all possible strings?

</details>

---

## ✅ My Solution

See [`solution.cpp`](./solution.cpp)

---

*Synced automatically from [LeetCode](https://leetcode.com/problems/find-unique-binary-string/) · Submission ID: 1100158785*
