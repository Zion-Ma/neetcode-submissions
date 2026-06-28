class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        coins.sort()
        for i in range(1, amount + 1):
            for c in coins:
                diff = i - c
                if diff >= 0:
                    dp[i] = min(dp[i], dp[diff] + 1)
        return dp[-1] if dp[-1] != float("inf") else -1