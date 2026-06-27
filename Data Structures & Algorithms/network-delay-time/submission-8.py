class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = {i:float("inf") if i != k else 0 for i in range(1, n + 1)}
        visited = {i:False for i in range(1, n + 1)}
        edges = defaultdict(list)
        for u, v, t in times:
            edges[u].append((v, t))
        pq = [(0, k)]
        while pq:
            curr_time, curr_node = heapq.heappop(pq)
            visited[curr_node] = True
            for neighbor, time in edges[curr_node]:
                if visited[neighbor]:
                    continue
                temp = curr_time + time
                if dist[neighbor] > temp:
                    dist[neighbor] = temp
                    heapq.heappush(pq, (temp, neighbor))
        m = max(dist.values())
        return m if m != float("inf") else -1
                