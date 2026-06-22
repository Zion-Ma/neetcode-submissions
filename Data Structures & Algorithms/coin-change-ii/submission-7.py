class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        def dfs(i: int, a: int) -> int:
            if a == 0:
                return 1
            if i >= len(coins):
                return 0
            if dp[i][a] != -1:
                return dp[i][a]
            diff = a - coins[i]
            res = 0
            if diff >= 0:
                res = dfs(i + 1, a) + dfs(i, diff)
                # res += dfs(i, diff)
                # dp[i][a] = dfs(i + 1, a) + dfs(i, diff)
            dp[i][a] = res
            return dp[i][a]
        return dfs(0, amount)
