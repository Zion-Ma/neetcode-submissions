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
        def union(i, j):
            p1, p2 = find(i), find(j)
            if p1 == p2: return 0
            if rank[p1] > rank[p2]:
                par[p2] = par[p1]
                rank[p1] += rank[p2]
            else:
                par[p1] = par[p2]
                rank[p2] += rank[p1]
            return 1
        res = n
        for i, j in edges:
            res -= union(i, j)
        return res
