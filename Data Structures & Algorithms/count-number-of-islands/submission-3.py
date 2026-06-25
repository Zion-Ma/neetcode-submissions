class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        def dfs(i: int, j: int) -> None:
            if (
                not m > i >= 0 or\
                not n > j >= 0 or\
                grid[i][j] != "1"
            ): return
            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            return
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1
        return ans
