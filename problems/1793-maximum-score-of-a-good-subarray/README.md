# 1793. Maximum Score of a Good Subarray

🔴 **Difficulty:** Hard &nbsp;|&nbsp; 🏷️ **Topics:** `Array` `Two Pointers` `Binary Search` `Stack` `Monotonic Stack`

---

## 📝 Problem Description

You are given an array of integers `nums` **(0-indexed)** and an integer `k`.

The **score** of a subarray `(i, j)` is defined as `min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1)`. A **good** subarray is a subarray where `i <= k <= j`.

Return *the maximum possible **score** of a **good** subarray.*

 
Example 1:


```
**Input:** nums = [1,4,3,7,4,5], k = 3
**Output:** 15
**Explanation:** The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15.
```


Example 2:


```
**Input:** nums = [5,5,4,5,4,1,1,1], k = 0
**Output:** 20
**Explanation:** The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.
```


 
**Constraints:**


	- `1 <= nums.length <= 105`
	- `1 <= nums[i] <= 2 * 104`
	- `0 <= k < nums.length`

## 💡 Hints

<details>
<summary>Show hints</summary>

1. Try thinking about the prefix before index k and the suffix after index k as two separate arrays.
2. Using two pointers or binary search, we can find the maximum prefix of each array where the numbers are less than or equal to a certain value

</details>

---

## ✅ My Solution

See [`solution.cpp`](./solution.cpp)

---

*Synced automatically from [LeetCode](https://leetcode.com/problems/maximum-score-of-a-good-subarray/) · Submission ID: 1081474620*
