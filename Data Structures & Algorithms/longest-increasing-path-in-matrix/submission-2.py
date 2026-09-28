class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        def dfs(i: int, j: int, prev: int) -> int:
            if (not 0 <= i < m or not 0 <= j < n or matrix[i][j] <= prev):
                return 0
            if dp[i][j] == -1:
                dp[i][j] = 1 + max(
                    dfs(i + 1, j, matrix[i][j]),
                    dfs(i - 1, j, matrix[i][j]),
                    dfs(i, j + 1, matrix[i][j]),
                    dfs(i, j - 1, matrix[i][j])
                )
            return dp[i][j]
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j, -1))
        return ans
