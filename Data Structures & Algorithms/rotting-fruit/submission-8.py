class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = []
        fresh = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        time = 0
        direc = [(0 ,1), (0, -1), (1, 0), (-1, 0)]
        while queue and fresh > 0:
            time += 1
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                for dx, dy in direc:
                    i, j = x + dx, y + dy
                    if not m > i >= 0 or not n > j >= 0 or grid[i][j] != 1:
                        continue
                    queue.append((i, j))
                    grid[i][j] = 2
                    fresh -= 1
        return time if fresh == 0 else -1
