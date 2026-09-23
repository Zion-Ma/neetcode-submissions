class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        source = deque()
        shift = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        time = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    source.append((i, j))
        while fresh > 0 and source:
            time += 1
            l = len(source)
            for _ in range(l):
                r, c = source.popleft()
                for dr, dc in shift:
                    x, y = r + dr, c + dc
                    if (x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 1):
                        continue
                    grid[x][y] = 2
                    fresh -= 1
                    source.append((x, y))
        return -1 if fresh > 0 else time
        
