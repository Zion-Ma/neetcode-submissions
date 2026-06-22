class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        for c in range(len(coins) - 1, -1, -1):
            for a in range(1, amount + 1):
                diff = a - coins[c]
                if diff >= 0:
                    dp[c][a] = dp[c + 1][a]
                    dp[c][a] += dp[c][diff]
        return dp[0][-1]