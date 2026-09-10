class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        coins.sort()
        for n in range(1, amount + 1):
            for c in coins:
                diff = n - c
                if diff >= 0:
                    dp[n] = min(dp[n], 1 + dp[diff])
        return dp[-1] if dp[-1] != float("inf") else -1