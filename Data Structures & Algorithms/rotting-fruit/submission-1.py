class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        miniute, fresh = 0, 0
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
        direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue and fresh > 0:
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                for x, y in direct:
                    row, col = i + x, j + y
                    if (
                        0 <= row < m and \
                        0 <= col < n and \
                        grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh -= 1
            miniute += 1
        return miniute if fresh == 0 else -1