class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            # temp = dp.copy()
            for i in range(1, amount + 1):
                diff = i - c
                if diff >= 0:
                    dp[i] += dp[diff]
        return dp[-1]

