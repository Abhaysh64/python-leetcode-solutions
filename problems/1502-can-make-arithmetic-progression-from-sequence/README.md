# 1502. Can Make Arithmetic Progression From Sequence

🟢 **Difficulty:** Easy &nbsp;|&nbsp; 🏷️ **Topics:** `Array` `Sorting`

---

## 📝 Problem Description

A sequence of numbers is called an **arithmetic progression** if the difference between any two consecutive elements is the same.

Given an array of numbers `arr`, return `true` *if the array can be rearranged to form an **arithmetic progression**. Otherwise, return* `false`.

 
Example 1:


```
**Input:** arr = [3,5,1]
**Output:** true
**Explanation: **We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
```


Example 2:


```
**Input:** arr = [1,2,4]
**Output:** false
**Explanation: **There is no way to reorder the elements to obtain an arithmetic progression.
```


 
**Constraints:**


	- `2 <= arr.length <= 1000`
	- `-106 <= arr[i] <= 106`

## 💡 Hints

<details>
<summary>Show hints</summary>

1. Consider that any valid arithmetic progression will be in sorted order.
2. Sort the array, then check if the differences of all consecutive elements are equal.

</details>

---

## ✅ My Solution

See [`solution.cpp`](./solution.cpp)

---

*Synced automatically from [LeetCode](https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/) · Submission ID: 965287732*
