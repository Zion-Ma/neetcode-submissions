class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        fresh = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        time = 0
        direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue and fresh > 0:
            time += 1
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                for x, y in direct:
                    r, c = i + x, j + y
                    if (
                        not 0 <= r < m or
                        not 0 <= c < n or
                        grid[r][c] != 1
                    ):
                        continue
                    fresh -= 1
                    queue.append((r, c))
                    grid[r][c] = 2
        return time if fresh == 0 else -1