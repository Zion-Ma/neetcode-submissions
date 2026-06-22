class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [float("inf") for _ in range((n1 + 1))]
        dp[-1] = 0
        for i in range(n1):
            dp[i] = n1 - i
        for i in range(n2 - 1, -1, -1):
            nextDP = [float("inf") for _ in range((n1 + 1))]
            nextDP[-1] = n2 - i
            for j in range(n1 - 1, -1, -1):
                if word2[i] == word1[j]:
                    nextDP[j] = dp[j + 1]
                else:
                    nextDP[j] = 1 + min(nextDP[j + 1], dp[j], dp[j + 1])
            dp = nextDP
        return dp[0]