class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [0 for _ in range(amount + 1)] 
        dp[0] = 1
        for c in range(len(coins) - 1, -1, -1):
            newDp = dp.copy()
            for a in range(1, amount + 1):
                diff = a - coins[c]
                if diff >= 0:
                    newDp[a] += newDp[diff]
            dp = newDp
        return dp[-1]