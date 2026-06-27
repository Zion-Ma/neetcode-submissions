class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = {i:float("inf") for i in range(n)}
        dist[0] = 0
        unvisited = set(range(n))
        curr = 0
        edges, cost = 0, 0
        while edges < n - 1:
            x, y = points[curr]
            unvisited.remove(curr)
            Next = -1
            for i in unvisited:
                u, v = points[i]
                curr_dist = abs(x - u) + abs(y - v)
                dist[i] = min(dist[i],  curr_dist)
                if Next == -1 or dist[Next] > dist[i]:
                    Next = i
            curr = Next
            cost += dist[Next]
            edges += 1
        return cost