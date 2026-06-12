class Solution:
    def depthUsingDFS(self, adj, src_node, parent_node):
        max_depth = 0

        for nbr_node in adj[src_node]:
            if nbr_node != parent_node:
                max_depth = max(
                    max_depth,
                    self.depthUsingDFS(adj, nbr_node, src_node) + 1
                )

        return max_depth

    def assignEdgeWeights(self, edges):
        n = len(edges) + 1

        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        max_depth = self.depthUsingDFS(adj, 1, 0)

        MOD = 10**9 + 7
        ans = 1
        base = 2
        exp = max_depth - 1

        while exp > 0:
            if exp & 1:
                ans = (ans * base) % MOD

            base = (base * base) % MOD
            exp >>= 1

        return ans