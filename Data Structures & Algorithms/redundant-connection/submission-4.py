class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(i):
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            p, q = find(i), find(j)
            if p == q:
                return True
            if rank[p] > rank[q]:
                parent[q] = parent[p]
                rank[p] += rank[q]
            else:
                parent[p] = parent[q]
                rank[q] += rank[p]
            return False
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        for src, dst in edges:
            if union(dst, src):
                return [src, dst]