# 0560. Subarray Sum Equals K

🟡 **Difficulty:** Medium &nbsp;|&nbsp; 🏷️ **Topics:** `Array` `Hash Table` `Prefix Sum`

---

## 📝 Problem Description

Given an array of integers `nums` and an integer `k`, return *the total number of subarrays whose sum equals to* `k`.

A subarray is a contiguous **non-empty** sequence of elements within an array.

 
Example 1:

```
**Input:** nums = [1,1,1], k = 2
**Output:** 2
```
Example 2:

```
**Input:** nums = [1,2,3], k = 3
**Output:** 2
```

 
**Constraints:**


	- `1 <= nums.length <= 2 * 104`
	- `-1000 <= nums[i] <= 1000`
	- `-107 <= k <= 107`

## 💡 Hints

<details>
<summary>Show hints</summary>

1. Will Brute force work here? Try to optimize it.
2. Can we optimize it by using some extra space?
3. What about storing sum frequencies in a hash table? Will it be useful?
4. sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1.

Can we use this property to optimize it.

</details>

---

## ✅ My Solution

See [`solution.cpp`](./solution.cpp)

---

*Synced automatically from [LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/) · Submission ID: 935963703*
