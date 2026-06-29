class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices) + 2)]
        for i in range(len(prices) - 1, -1, -1):
            for canBuy in [0, 1]:
                skip = dp[i + 1][canBuy]
                if canBuy:
                    today_decision = dp[i + 1][0] - prices[i]
                else:
                    today_decision = dp[i + 2][1] + prices[i]
                dp[i][canBuy] = max(today_decision, skip)
        return dp[0][1]
