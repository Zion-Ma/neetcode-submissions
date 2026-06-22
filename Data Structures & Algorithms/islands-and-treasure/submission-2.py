class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        queue = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        level = 0
        direc = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                x, y = curr[0], curr[1]
                grid[x][y] = level
                for dx, dy in direc:
                    i, j = x + dx, y + dy
                    if not m > i >= 0 or not n > j >= 0:
                        continue
                    if (i, j) not in visited and grid[i][j] != -1:
                        visited.add((i, j))
                        queue.append((i, j))
            level += 1