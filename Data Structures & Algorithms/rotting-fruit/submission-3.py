class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        time, fresh, queue = 0, 0, []
        direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        while queue and fresh > 0:
            time += 1
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                for x, y in direc:
                    r, c = i + x, j + y
                    if (
                        0 <= r < m and
                        0 <= c < n and
                        grid[r][c] == 1
                    ):
                        grid[r][c] = 2
                        fresh -= 1
                        queue.append((r, c))
        return time if fresh == 0 else -1