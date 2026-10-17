class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        minHeap = [(0, 0, 0)]
        visited = set()
        direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if (r, c) == (rows - 1, cols - 1):
                return diff
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for dr, dc in direc:
                x, y = r + dr, c + dc
                if (not 0 <= x < rows or not 0 <= y < cols or (x, y) in visited):
                    continue
                curr_diff = max(diff, abs(heights[r][c] - heights[x][y]))
                heapq.heappush(minHeap, (curr_diff, x, y))
                