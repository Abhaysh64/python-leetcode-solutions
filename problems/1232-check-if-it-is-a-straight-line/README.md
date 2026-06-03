# 1232. Check If It Is a Straight Line

🟢 **Difficulty:** Easy &nbsp;|&nbsp; 🏷️ **Topics:** `Array` `Math` `Geometry`

---

## 📝 Problem Description

You are given an integer array `coordinates`, `coordinates[i] = [x, y]`, where `[x, y]` represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 
Example 1:




```
**Input:** coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
**Output:** true
```


Example 2:

****


```
**Input:** coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
**Output:** false
```


 
**Constraints:**


	- `2 <= coordinates.length <= 1000`
	- `coordinates[i].length == 2`
	- `-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4`
	- `coordinates` contains no duplicate point.

## 💡 Hints

<details>
<summary>Show hints</summary>

1. If there're only 2 points, return true.
2. Check if all other points lie on the line defined by the first 2 points.
3. Use cross product to check collinearity.

</details>

---

## ✅ My Solution

See [`solution.cpp`](./solution.cpp)

---

*Synced automatically from [LeetCode](https://leetcode.com/problems/check-if-it-is-a-straight-line/) · Submission ID: 964086897*
