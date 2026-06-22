class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        def find(i):
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            p, q = parent[i], parent[j]
            if p == q:
                return 0
            if rank[p] > rank[q]:
                parent[q] = parent[p]
                rank[p] += rank[q]
            else:
                parent[p] = parent[q]
                rank[q] += rank[p]
            return 1
        parent = [i for i in range(n)]
        rank = [1] * n
        res = n
        for i, j in edges:
            res -= union(i, j)
        return res == 1