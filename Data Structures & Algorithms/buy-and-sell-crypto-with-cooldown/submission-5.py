class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp: dist[tupel[int, bool], int] = dict()
        def dfs(i: int, haveCoin: bool) -> int:
            if i >= len(prices):
                return 0
            if (i, haveCoin) in dp:
                return dp[(i, haveCoin)]
            coolDown = dfs(i + 1, haveCoin)
            todayDec = None
            if haveCoin:
                # sell
                todayDec = dfs(i + 2, not haveCoin) + prices[i]
            else:
                todayDec = dfs(i + 1, not haveCoin) - prices[i]
            dp[(i, haveCoin)] = max(todayDec, coolDown) 
            return dp[(i, haveCoin)]
        return dfs(0, False)