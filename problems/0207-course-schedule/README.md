# 0207. Course Schedule

🟡 **Difficulty:** Medium &nbsp;|&nbsp; 🏷️ **Topics:** `Depth-First Search` `Breadth-First Search` `Graph Theory` `Topological Sort`

---

## 📝 Problem Description

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.


	- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.


Return `true` if you can finish all courses. Otherwise, return `false`.

 
Example 1:


```
**Input:** numCourses = 2, prerequisites = [[1,0]]
**Output:** true
**Explanation:** There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
```


Example 2:


```
**Input:** numCourses = 2, prerequisites = [[1,0],[0,1]]
**Output:** false
**Explanation:** There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```


 
**Constraints:**


	- `1 <= numCourses <= 2000`
	- `0 <= prerequisites.length <= 5000`
	- `prerequisites[i].length == 2`
	- `0 <= ai, bi < numCourses`
	- All the pairs prerequisites[i] are **unique**.

## 💡 Hints

<details>
<summary>Show hints</summary>

1. This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
2. <a href="https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/03Graphs.pdf" target="_blank">Topological Sort via DFS</a> - A great tutorial explaining the basic concepts of Topological Sort.
3. Topological sort could also be done via <a href="http://en.wikipedia.org/wiki/Topological_sorting#Algorithms" target="_blank">BFS</a>.

</details>

---

## ✅ My Solution

See [`solution.cpp`](./solution.cpp)

---

*Synced automatically from [LeetCode](https://leetcode.com/problems/course-schedule/) · Submission ID: 993560906*
