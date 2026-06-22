class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.curr_area = 0
        max_area = 0
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if not 0 <= i < m or not 0 <= j < n or grid[i][j] == 0:
                return
            self.curr_area += 1
            grid[i][j] = 0
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    max_area = max(max_area, self.curr_area)
                    self.curr_area = 0
        return max_area

        