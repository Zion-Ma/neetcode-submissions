class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        unvisited = set(range(n))
        dist = {i:float("inf") for i in range(n)}
        pq = [(0, 0)]
        cost, edges = 0, 0
        while edges < n - 1:
            curr_dist, p = heapq.heappop(pq)
            if p not in unvisited:
                continue
            x, y = points[p]
            unvisited.remove(p)
            Min, Next = float("inf"), -1
            for i in unvisited:
                u, v = points[i]
                temp = abs(x - u) + abs(y - v)
                dist[i] = min(dist[i], temp)
                if dist[i] < Min:
                    Min, Next = dist[i], i
            # if Next != -1:
            heapq.heappush(pq, (Min, Next))
            cost += Min
            edges += 1
        return cost

