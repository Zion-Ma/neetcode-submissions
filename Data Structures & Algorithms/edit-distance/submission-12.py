class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        dp = [float("inf")] * (n + 1)
        # for i in range(m + 1):
        #     dp[i][n] = m - i
        for j in range(n + 1):
            dp[j] = n - j
        for i in range(m - 1, -1, -1):
            temp = dp.copy()
            temp[-1] = m - i
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    temp[j] = dp[j + 1]
                else:
                    temp[j] = 1 + min(dp[j], temp[j + 1], dp[j + 1])
            dp = temp
        return dp[0]
                