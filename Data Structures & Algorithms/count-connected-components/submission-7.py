class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [0 for _ in range(n)]
        def union(i, j):
            p, q = find(i), find(j)
            if p == q:
                return 0
            if rank[p] > rank[q]:
                parent[q] = p
                rank[p] += rank[q]
            else:
                parent[p] = q
                rank[q] += rank[p]
            return 1

        def find(i):
            res = i
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
            
        res = n
        for i, j in edges:
            res -= union(i, j)
        return res
