class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [[0 for _ in range(amount + 1)]] * (len(coins) + 1)
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        for i in range(len(coins) - 1, -1, -1):
            for j in range(1, amount + 1):
                diff = j - coins[i]
                if diff >= 0:
                    dp[i][j] = dp[i + 1][j]
                    dp[i][j] += dp[i][diff]
        return dp[0][amount]