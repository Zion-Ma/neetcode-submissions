class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp: dict[tuple[int, bool], int] = dict()
        def dfs(i: int, canBuy: bool) -> int:
            if i >= len(prices):
                return 0
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]
            skip = dfs(i + 1, canBuy)
            today_decision = 0
            if canBuy:
                today_decision = dfs(i + 1, not canBuy) - prices[i]
            else:
                today_decision = dfs(i + 2, not canBuy) + prices[i]
            best = max(skip, today_decision)
            dp[(i, canBuy)] = best
            return best
        return dfs(0, True)