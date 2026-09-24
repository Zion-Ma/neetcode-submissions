class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        coins.sort()
        for c in coins:
            new_dp = dp
            for a in range(1, amount + 1):
                diff = a - c
                if diff >= 0:
                    new_dp[a] += new_dp[diff]
            dp = new_dp
        return dp[amount]