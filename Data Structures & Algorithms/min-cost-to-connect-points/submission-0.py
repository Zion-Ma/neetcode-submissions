import itertools

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(i):
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            p, q = find(i), find(j)
            if p == q: return False
            if rank[p] > rank[q]:
                parent[q] = parent[p]
                rank[p] += rank[q]
            else:
                parent[p] = parent[q]
                rank[q] += rank[p]
            return True
        minHeap = []
        for i, j in itertools.combinations(range(len(points)), 2):
            x, y = points[i]
            u, v = points[j]
            dist = abs(x - u) + abs(y - v)
            heapq.heappush(minHeap, (dist, (i, j)))
        parent = [i for i in range(len(points))]
        rank = [0 for _ in range(len(points))]
        res = len(points)
        length = 0
        while res > 1:
            dist, (i, j) = heapq.heappop(minHeap)
            if not union(i, j):
                continue
            length += dist
            res -= 1
        return length

        
