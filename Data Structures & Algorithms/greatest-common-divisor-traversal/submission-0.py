class DSU:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.count = n
    
    def find(self, i: int) -> int:
        if self.parent[i] != self.parent[self.parent[i]]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        p1, p2 = self.find(i), self.find(j)
        if p1 == p2:
            return
        s1, s2 = self.size[p1], self.size[p2]
        if s1 > s2:
            self.size[p1] += s2
            self.parent[p2] = p1
        else:
            self.size[p2] += s1
            self.parent[p1] = p2
        self.count -= 1
        return

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        factor_index = dict()
        dsu = DSU(len(nums))
        for i, n in enumerate(nums):
            f = 2
            while f * f <= n:
                if n % f == 0:
                    if f in factor_index:
                        dsu.union(i, factor_index[f])
                    else:
                        factor_index[f] = i
                while n % f == 0:
                    n //= f
                f += 1
            if n > 1:
                if n in factor_index:
                    dsu.union(i, factor_index[n])
                else:
                    factor_index[n] = i
        return dsu.count == 1


