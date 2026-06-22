class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [n - j for j in range(n + 1)]
        for i in range(m - 1, -1, -1):
            nextDP = [float("inf")] * (n + 1)
            nextDP[-1] = m - i
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    nextDP[j] = dp[j + 1]
                else:
                    nextDP[j] = 1 + min(dp[j], nextDP[j + 1], dp[j + 1])
            dp = nextDP
        return dp[0]
