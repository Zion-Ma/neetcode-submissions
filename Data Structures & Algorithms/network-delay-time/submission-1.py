class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i:[] for i in range(1, n + 1)}
        for x, y, t in times:
            graph[x].append((y, t))
        visit = set()
        pq = [(0, k)]
        t = 0
        while pq:
            curr_dist, u = heapq.heappop(pq)
            if u in visit:
                continue
            visit.add(u)
            t = max(t, curr_dist)
            for v, dist in graph[u]:
                if v not in visit:
                    # visit.add(v)
                    heapq.heappush(pq, (curr_dist + dist, v))
        return t if len(visit) == n else -1