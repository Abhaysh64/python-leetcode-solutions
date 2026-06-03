# 1512. Number of Good Pairs

🟢 **Difficulty:** Easy &nbsp;|&nbsp; 🏷️ **Topics:** `Array` `Hash Table` `Math` `Counting`

---

## 📝 Problem Description

Given an array of integers `nums`, return *the number of **good pairs***.

A pair `(i, j)` is called *good* if `nums[i] == nums[j]` and `i` < `j`.

 
Example 1:


```
**Input:** nums = [1,2,3,1,1,3]
**Output:** 4
**Explanation:** There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
```


Example 2:


```
**Input:** nums = [1,1,1,1]
**Output:** 6
**Explanation:** Each pair in the array are *good*.
```


Example 3:


```
**Input:** nums = [1,2,3]
**Output:** 0
```


 
**Constraints:**


	- `1 <= nums.length <= 100`
	- `1 <= nums[i] <= 100`

## 💡 Hints

<details>
<summary>Show hints</summary>

1. Count how many times each number appears. If a number appears n times, then n * (n – 1) // 2 good pairs can be made with this number.

</details>

---

## ✅ My Solution

See [`solution.cpp`](./solution.cpp)

---

*Synced automatically from [LeetCode](https://leetcode.com/problems/number-of-good-pairs/) · Submission ID: 1066018577*
