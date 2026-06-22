class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        path = [float("inf")] * (n + 1)
        edges = {i:[] for i in range(n + 1)}
        for u, v, t in times:
            edges[u].append((v, t))
        path[k] = 0
        pq = [(0, k)]
        while pq:
            curr_t, curr = heapq.heappop(pq)
            for v, t in edges[curr]:
                if path[v] > path[curr] + t:
                    path[v] = path[curr] + t
                    heapq.heappush(pq, (path[v], v))
        m = max(path[1:])
        return m if m != float("inf") else -1
        
        