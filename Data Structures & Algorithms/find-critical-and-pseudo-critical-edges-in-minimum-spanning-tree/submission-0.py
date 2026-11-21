class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, v: int) -> int:
        if self.parent[v] != self.parent[self.parent[v]]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1: int, v2: int) -> bool:
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False
        s1, s2 = self.size[p1], self.size[p2]
        if s1 > s2:
            self.size[p1] += s2
            self.parent[p2] = p1
        else:
            self.size[p2] += s1
            self.parent[p1] = p2
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        critical = []
        pseudo = []
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key = lambda x:x[2])
        uf = UnionFind(n)
        mst_weight = 0
        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                mst_weight += w
        for n1, n2, w1, i1 in edges:
            # probing for critical
            uf = UnionFind(n)
            curr_st_weight = 0
            for v1, v2, w2, i2 in edges:
                if i1 == i2:
                    continue
                if uf.union(v1, v2):
                    curr_st_weight += w2
            if max(uf.size) != n or curr_st_weight > mst_weight:
                critical.append(i1)
                continue
            # probing for pseudo
            uf = UnionFind(n)
            uf.union(n1, n2)
            curr_st_weight = w1
            for v1, v2, w2, i2 in edges:
                if uf.union(v1, v2):
                    curr_st_weight += w2
            if curr_st_weight == mst_weight:
                pseudo.append(i1)
        return [critical, pseudo]

