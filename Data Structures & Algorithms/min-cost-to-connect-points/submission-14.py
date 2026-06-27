class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        unvisited = set(range(n))
        dist = {i:float("inf") for i in range(n)}
        curr = 0
        cost, edges = 0, 0
        while edges < n - 1:
            x, y = points[curr]
            unvisited.remove(curr)
            Next = -1
            for i in unvisited:
                u, v = points[i]
                curr_dist = abs(x - u) + abs(y - v)
                dist[i] = min(dist[i], curr_dist)
                if Next == -1 or dist[i] < dist[Next]:
                    Next = i
            cost += dist[Next]
            curr = Next
            edges += 1
        return cost

