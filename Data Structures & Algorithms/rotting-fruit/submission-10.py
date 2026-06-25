class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        m, n = len(grid), len(grid[0])
        fresh, time = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
        while queue and fresh > 0:
            time += 1
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r, c = i + x, j + y
                    if (
                        not m > r >= 0 or\
                        not n > c >= 0 or\
                        grid[r][c] != 1
                    ): continue
                    fresh -= 1
                    queue.append((r, c))
                    grid[r][c] = 2
        return time if fresh == 0 else -1