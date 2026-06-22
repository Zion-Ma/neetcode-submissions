class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = prices.__len__()
        dp = [[0] * 2 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for buying in [0, 1]:
                cooldown = dp[i + 1][buying] if i + 1 < n else 0
                if buying:
                    buy = dp[i + 1][0] - prices[i] if i + 1 < n else -prices[i]
                    dp[i][1] = max(buy, cooldown)
                else:
                    sell = dp[i + 2][1] + prices[i] if i + 2 < n else prices[i]
                    dp[i][0] = max(sell, cooldown)
        return dp[0][1]
        