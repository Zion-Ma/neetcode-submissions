class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices))]
        for i in range(len(prices) - 1, -1, -1):
            for haveStock in [0, 1]:
                coolDown = dp[i + 1][haveStock] if i + 1 < len(prices) else 0
                todayDec = -1
                if haveStock:
                    # sell
                    todayDec = (dp[i + 2][not haveStock] if i + 2 < len(prices) else 0) + prices[i]
                else:
                    # buy
                    todayDec = (dp[i + 1][not haveStock] if i + 1 < len(prices) else 0) - prices[i]
                dp[i][haveStock] = max(todayDec, coolDown)
        return dp[0][0]
