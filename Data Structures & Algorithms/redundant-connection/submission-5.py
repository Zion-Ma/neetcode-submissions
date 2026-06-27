class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for u, v in edges:
            if not dsu.union(u - 1, v - 1):
                return [u, v]

class DSU:
    def __init__(self, n: int) -> int:
        self.size = [1] * n
        self.parents = list(range(n))
        self.components = n
    
    def find(self, i: int) -> int:
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]
    
    def union(self, i: int, j: int) -> bool:
        p, q = self.find(i), self.find(j)
        if p == q:
            return False
        if self.size[p] > self.size[q]:
            self.parents[q] = p
            self.size[p] += self.size[q]
        else:
            self.parents[p] = q
            self.size[q] += self.size[p]
        self.components -= 1
        return True