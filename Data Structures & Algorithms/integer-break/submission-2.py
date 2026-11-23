class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        dp[n] = 0
        for num in range(2, n + 1):
            for i in range(1, num):
                dp[num] = max(dp[num], dp[i] * dp[num - i])
        return dp[n]