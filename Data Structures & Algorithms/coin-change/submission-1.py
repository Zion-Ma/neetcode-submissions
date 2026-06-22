"""
check for number <= amount, how many possible ways to achieve amount
1. initilize dp, an array of length (amount + 1), each element as inf
2. set dp[0] to 1
3. check the rest of dp, dp[i] = min(dp[i], 1 + dp[amount - coins[j]])
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[amount] if dp[amount] != float("inf") else -1