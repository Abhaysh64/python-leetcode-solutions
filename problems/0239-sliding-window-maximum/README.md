# 0239. Sliding Window Maximum

🔴 **Difficulty:** Hard &nbsp;|&nbsp; 🏷️ **Topics:** `Array` `Queue` `Sliding Window` `Heap (Priority Queue)` `Monotonic Queue`

---

## 📝 Problem Description

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return *the max sliding window*.

 
Example 1:


```
**Input:** nums = [1,3,-1,-3,5,3,6,7], k = 3
**Output:** [3,3,5,5,6,7]
**Explanation:** 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       **3**
 1 [3  -1  -3] 5  3  6  7       **3**
 1  3 [-1  -3  5] 3  6  7      ** 5**
 1  3  -1 [-3  5  3] 6  7       **5**
 1  3  -1  -3 [5  3  6] 7       **6**
 1  3  -1  -3  5 [3  6  7]      **7**
```


Example 2:


```
**Input:** nums = [1], k = 1
**Output:** [1]
```


 
**Constraints:**


	- `1 <= nums.length <= 105`
	- `-104 <= nums[i] <= 104`
	- `1 <= k <= nums.length`

## 💡 Hints

<details>
<summary>Show hints</summary>

1. How about using a data structure such as deque (double-ended queue)?
2. The queue size need not be the same as the window’s size.
3. Remove redundant elements and the queue should store only elements that need to be considered.

</details>

---

## ✅ My Solution

See [`solution.cpp`](./solution.cpp)

---

*Synced automatically from [LeetCode](https://leetcode.com/problems/sliding-window-maximum/) · Submission ID: 1023421737*
