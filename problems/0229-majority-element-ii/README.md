# 0229. Majority Element II

🟡 **Difficulty:** Medium &nbsp;|&nbsp; 🏷️ **Topics:** `Array` `Hash Table` `Sorting` `Counting`

---

## 📝 Problem Description

Given an integer array of size `n`, find all elements that appear more than `&lfloor; n/3 &rfloor;` times.

 
Example 1:


```
**Input:** nums = [3,2,3]
**Output:** [3]
```


Example 2:


```
**Input:** nums = [1]
**Output:** [1]
```


Example 3:


```
**Input:** nums = [1,2]
**Output:** [1,2]
```


 
**Constraints:**


	- `1 <= nums.length <= 5 * 104`
	- `-109 <= nums[i] <= 109`


 
**Follow up:** Could you solve the problem in linear time and in `O(1)` space?

## 💡 Hints

<details>
<summary>Show hints</summary>

1. Think about the possible number of elements that can appear more than ⌊ n/3 ⌋ times in the array.
2. It can be at most two. Why?
3. Consider using Boyer-Moore Voting Algorithm, which is efficient for finding elements that appear more than a certain threshold.

</details>

---

## ✅ My Solution

See [`solution.cpp`](./solution.cpp)

---

*Synced automatically from [LeetCode](https://leetcode.com/problems/majority-element-ii/) · Submission ID: 1067900222*
