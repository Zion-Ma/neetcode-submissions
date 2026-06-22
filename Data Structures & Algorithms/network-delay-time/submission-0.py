class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i:[] for i in range(n + 1)}
        for x, y, t in times:
            graph[x].append((y, t))
        dist = [float("inf") if i != k else 0 for i in range(n + 1)]
        pq = [(0, k)]
        # time = 0
        while pq:
            curr_dist, u = heapq.heappop(pq)
            for v, weight in graph[u]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
        m = max(dist[1:])
        return m if m != float("inf") else -1