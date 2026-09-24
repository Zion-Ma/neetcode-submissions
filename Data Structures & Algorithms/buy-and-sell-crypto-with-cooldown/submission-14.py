class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp1 = [0] * 2
        dp2 = [0] * 2
        for i in range(len(prices) - 1, -1, -1):
            new_dp = [0] * 2
            for canbuy in [0, 1]:
                cooldown = dp1[canbuy]
                if canbuy:
                    profit = dp1[0] - prices[i]
                else:
                    profit = dp2[1] + prices[i]
                new_dp[canbuy] = max(profit, cooldown)
            dp2 = dp1
            dp1 = new_dp
        return dp1[1]
