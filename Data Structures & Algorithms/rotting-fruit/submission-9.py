class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = []
        m, n = len(grid), len(grid[0])
        fresh, time = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    visited.add((i, j))
                    queue.append((i, j))
        if fresh == 0:
            return 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                grid[i][j] = 2
                for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r, c = i + x, j + y
                    if (
                        not m > r >= 0 or\
                        not n > c >= 0 or\
                        grid[r][c] != 1 or\
                        (r, c) in visited
                    ): continue
                    fresh -= 1
                    queue.append((r, c))
                    visited.add((r, c))
            time += 1
        return time - 1 if fresh == 0 else -1