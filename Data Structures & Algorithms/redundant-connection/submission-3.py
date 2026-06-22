class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [0] * (len(edges) + 1)
        def find(i):
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            p, q = find(i), find(j)
            if p == q:
                return False
            if rank[p] > rank[q]:
                parent[q] = parent[p]
                rank[p] += rank[q]
            else:
                parent[p] = parent[q]
                rank[q] += rank[p]
            return True
        for x, y in edges:
            if not union(x, y):
                return [x, y]