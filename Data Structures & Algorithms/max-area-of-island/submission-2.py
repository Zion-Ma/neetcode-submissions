from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_area = 0
        self.area = 0
        def dfs(i: int, j: int) -> None:
            # boundary or water check
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != 1:
                return

            # mark visited
            grid[i][j] = 0
            # update global max
            self.area += 1
            # explore 4 directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    max_area = max(max_area, self.area)
                    self.area = 0

        return max_area
