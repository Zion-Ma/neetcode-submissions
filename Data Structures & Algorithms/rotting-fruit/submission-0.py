class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = []
        miniute = 0
        self.total_fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    self.total_fresh += 1
        def add(i, j):
            if not 0 <= i < m or not 0 <= j < n or grid[i][j] != 1:
                return
            queue.append((i, j))
            self.total_fresh -= 1
            grid[i][j] = 2
        while queue and self.total_fresh > 0:
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                add(i + 1, j)
                add(i - 1, j)
                add(i, j + 1)
                add(i, j - 1)
            miniute += 1
        return miniute if self.total_fresh == 0 else -1
        