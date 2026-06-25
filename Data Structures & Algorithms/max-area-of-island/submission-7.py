class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        Max = 0
        def dfs(i: int, j: int) -> int:
            if (
                not m > i >= 0 or\
                not n > j >= 0 or\
                grid[i][j] != 1
            ): return 0
            grid[i][j] = 0
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    Max = max(Max, dfs(i, j))
        return Max
