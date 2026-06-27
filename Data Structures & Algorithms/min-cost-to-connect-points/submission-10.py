class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        unvisited = set(range(len(points)))
        pq = [(0, 0)]
        cost = 0
        while len(unvisited) > 0:
            curr_dist, p = heapq.heappop(pq)
            if p not in unvisited:
                continue
            cost += curr_dist
            unvisited.remove(p)
            x, y = points[p]
            Min, Next = float("inf"), -1
            for i in unvisited:
                u, v = points[i]
                dist = abs(x - u) + abs(y - v)
                heapq.heappush(pq, (dist, i))
        return cost

