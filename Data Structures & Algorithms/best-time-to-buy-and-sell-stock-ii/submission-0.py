class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = dict()
        def dfs(i: int, canbuy: bool) -> int:
            if i >= len(prices):
                return 0
            if (i, canbuy) in dp:
                return dp[(i, canbuy)]
            skip = dfs(i + 1, canbuy)
            if canbuy:
                profit = dfs(i + 1, not canbuy) - prices[i]
            else:
                profit = dfs(i + 1, not canbuy) + prices[i]
            dp[(i, canbuy)] = max(skip, profit)
            return dp[(i, canbuy)]
        return dfs(0, True)