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
                    visited.add((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        time = -1
        direc = [(0 ,1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                x, y = curr[0], curr[1]
                grid[x][y] = 2
                for dx, dy in direc:
                    i, j = x + dx, y + dy
                    if not m > i >= 0 or not n > j >= 0 or grid[i][j] != 1 or (i, j) in visited:
                        continue
                    queue.append((i, j))
                    visited.add((i, j))
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1
