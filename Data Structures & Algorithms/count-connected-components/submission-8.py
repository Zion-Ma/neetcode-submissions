class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        para = [i for i in range(n)]
        rank = [0] * n
        res = n
        def find(i):
            r = i
            while r != para[r]:
                para[r] = para[para[r]]
                r = para[r]
            return r
        def union(i, j):
            p, q = find(i), find(j)
            if p == q:
                return 0
            if rank[p] > rank[q]:
                para[q] = p
                rank[p] += rank[q]
            else:
                para[p] = q
                rank[q] += rank[p]
            return 1
        for x, y in edges:
            res -= union(x, y)
        return res