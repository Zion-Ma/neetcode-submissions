class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        def find(i: int) -> int:
            res = i
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        def union(i: int, j: int) -> int:
            p, q = find(i), find(j)
            if p == q:
                return 0
            if rank[p] > rank[q]:
                par[q] = p
                rank[p] += rank[q]
            else:
                par[p] = q
                rank[q] += rank[p]
            return 1
        res = n
        for i, j in edges:
            res -= union(i, j)
        return res