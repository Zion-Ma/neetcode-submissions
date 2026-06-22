class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        m, n = len(matrix), len(matrix[0])
        def dfs(i, j, prev):
            if not 0 <= i < m or not 0 <= j < n or matrix[i][j] <= prev:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            curr = matrix[i][j]
            dp[(i, j)] = max(dfs(i + 1, j, curr), dfs(i - 1, j, curr), dfs(i, j + 1, curr), dfs(i, j - 1, curr)) + 1
            return dp[(i, j)]
        ans = -1
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j, -1))
        return ans