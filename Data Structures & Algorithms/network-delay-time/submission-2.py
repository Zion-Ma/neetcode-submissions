"""
1. initial distance array with length of n, with each element, except for dist[k], as infinity, otherwise 0.
2. build pairwise graph with times
3. push (dist[k], k) to priority queue
4. pop top from pq
5. check every neighbor of top; if dist[neighbor] > dist[top] + edge(top, neighbor), update dist[neighbor] and push it to PQ
6. repeat 1 - 5 until empty PQ
"""

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf") for _ in range(n + 1)]
        dist[k] = 0
        graph = {i:[] for i in range(1, n + 1)}
        for u, v, t in times:
            graph[u].append((v, t))
        pq = [(0, k)]
        while pq:
            curr_dist, node = heapq.heappop(pq)
            for nei, nei_dist in graph[node]:
                if dist[nei] > dist[node] + nei_dist:
                    dist[nei] = dist[node] + nei_dist
                    heapq.heappush(pq, (dist[nei], nei))
        m = max(dist[1:])
        return m if m != float("inf") else -1
