class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [0] * n
        res = n
        
        def find(i):
            curr = i
            while curr != parent[curr]:
                parent[curr] = parent[parent[curr]]
                curr = parent[curr]
            return curr
        
        def union(i, j):
            p, q = find(i), find(j)
            if p == q:
                return 0
            if rank[p] > rank[q]:
                parent[q] = parent[p]
                rank[p] += rank[q]
            else:
                parent[p] = parent[q]
                rank[q] += rank[p]
            return 1
        for x, y in edges:
            res -= union(x, y)
        return res
