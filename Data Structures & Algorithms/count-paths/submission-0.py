class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        w = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            w[i][0] = 1
        for j in range(n):
            w[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                w[i][j] = w[i - 1][j] + w[i][j - 1]
        return w[m - 1][n - 1]