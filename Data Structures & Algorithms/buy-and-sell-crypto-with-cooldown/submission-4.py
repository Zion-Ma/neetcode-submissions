class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp: dict[tuple[int, bool], int] = dict()
        def dfs(i: int, haveCoin: bool) -> int:
            if i >= len(prices):
                return 0
            if (i, haveCoin) in dp:
                return dp[(i, haveCoin)]
            coolDown = dfs(i + 1, haveCoin)
            today = -1
            if haveCoin:
                # sell
                today = dfs(i + 2, not haveCoin) + prices[i]
            else:
                # buy
                today = dfs(i + 1, not haveCoin) - prices[i]
            dp[(i, haveCoin)] = max(today, coolDown)
            return dp[(i, haveCoin)]
        return dfs(0, False)