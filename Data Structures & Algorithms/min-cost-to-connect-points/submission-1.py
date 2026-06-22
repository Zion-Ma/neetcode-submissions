from itertools import combinations

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
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
        parent = [i for i in range(len(points))]
        rank = [0 for _ in range(len(points))]
        minHeap = []
        for p1, p2 in combinations(range(len(points)), 2):
            i, j = points[p1]
            u, v = points[p2]
            dist = abs(i - u) + abs(j - v)
            heapq.heappush(minHeap, (dist, (p1, p2)))
        res = len(points)
        length = 0
        while res > 1:
            dist, (i, j) = heapq.heappop(minHeap)
            if union(i, j):
                continue
            res -= 1
            length += dist
        return length