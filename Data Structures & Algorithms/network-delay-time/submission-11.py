class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * (n + 1)
        dist[k] = 0
        time = 0
        adj = defaultdict(list)
        seen = set()
        minHeap = []
        for u, v, t in times:
            adj[u].append((t, v))
        minHeap.append((0, k))
        while minHeap and len(seen) < n:
            d, u = heapq.heappop(minHeap)
            if u in seen:
                continue
            seen.add(u)
            time = d
            for t, v in adj[u]:
                w = dist[u] + t
                if w < dist[v]:
                    dist[v] = w
                    heapq.heappush(minHeap, (w, v))
        for val in dist[1:]:
            if val == float("inf"):
                return -1
        return time
                
