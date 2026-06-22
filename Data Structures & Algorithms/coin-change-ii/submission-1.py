class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            nextDP = dp.copy()
            for i, curr in enumerate(nextDP):
                if i >= c:
                    nextDP[i] += nextDP[i - c]
            dp = nextDP
        return dp[amount]