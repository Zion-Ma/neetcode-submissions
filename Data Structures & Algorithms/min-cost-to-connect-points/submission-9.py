class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * (n)
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self, u, v):
        p, q = self.find(u), self.find(v)
        if p == q:
            return False
        if self.rank[p] > self.rank[q]:
            self.parent[q] = self.parent[p]
            self.rank[p] += self.rank[q]
        else:
            self.parent[p] = self.parent[q]
            self.rank[q] += self.rank[p]
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)
        pq = []
        cost = 0
        unvisited = n
        for i in range(n):
            px, py = points[i]
            for j in range(i + 1, n):
                qx, qy = points[j]
                dist = abs(px - qx) + abs(py - qy)
                heapq.heappush(pq, (dist, i, j))
        while unvisited > 0 and pq:
            dist, i, j = heapq.heappop(pq)
            if not dsu.union(i, j):
                continue
            cost += dist
            unvisited -= 1
        return cost
        