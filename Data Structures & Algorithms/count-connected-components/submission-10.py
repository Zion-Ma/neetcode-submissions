class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u, v)
        return dsu.components

class DSU:
    def __init__(self, n: int) -> None:
        self.size = [1] * n
        self.parants = list(range(n))
        self.components = n
    
    def find(self, i: int) -> int:
        if self.parants[i] != i:
            self.parants[i] = self.find(self.parants[i])
        return self.parants[i]
    
    def union(self, i: int, j: int) -> None:
        p, q = self.find(i), self.find(j)
        if p == q:
            return 
        s1, s2 = self.size[p], self.size[q]
        if s1 > s2:
            self.parants[q] = p
            self.size[p] += self.size[q]
        else:
            self.parants[p] = q
            self.size[q] += self.size[p]
        self.components -= 1
        return

