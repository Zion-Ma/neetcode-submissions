class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[float("inf") for _ in range((n1 + 1))] for _ in range(n2 + 1)]
        dp[-1][-1] = 0
        for i in range(n1):
            dp[-1][i] = n1 - i
        for i in range(n2):
            dp[i][-1] = n2 - i
        for i in range(n2 - 1, -1, -1):
            for j in range(n1 - 1, -1, -1):
                if word2[i] == word1[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])
        return dp[0][0]