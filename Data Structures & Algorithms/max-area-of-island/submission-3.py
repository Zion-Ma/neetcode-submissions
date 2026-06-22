class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j) -> int:
            if (
                not 0 <= i < m or \
                not 0 <= j < n or \
                (i, j) in visit or \
                grid[i][j] != 1
            ):
                return 0
            visit.add((i, j))
            return (
                1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            )
        m, n = len(grid), len(grid[0])
        visit = set()
        area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = max(area, dfs(i, j))
        return area