class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [[float("inf")] * n for _ in range(n)]
        for u, v, t in times:
            dist[u - 1][v - 1] = t
        for i in range(n):
            dist[i][i] = 0
        for mid in range(n):
            for i in range(n):
                if i == mid: continue
                for j in range(n):
                    if dist[i][j] > dist[i][mid] + dist[mid][j]:
                        dist[i][j] = dist[i][mid] + dist[mid][j]
        m = max(dist[k - 1])
        return m if m != float("inf") else -1