class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        level = 0
        queue = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        while queue:
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                grid[i][j] = level
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    r, c = i + x, j + y
                    if (
                        not m > r >= 0 or\
                        not n > c >= 0 or\
                        grid[r][c] == -1 or\
                        (r, c) in visited
                    ): continue
                    visited.add((r, c))
                    queue.append((r, c))
            level += 1
        