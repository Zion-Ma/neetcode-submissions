class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int) -> None:
            if not m > i >= 0 or not n > j >= 0 or grid[i][j] != 1:
                return
            self.localArea += 1
            grid[i][j] = 0
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        maxArea = 0
        self.localArea = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    maxArea = max(maxArea, self.localArea)
                    self.localArea = 0
        return maxArea