class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, max_profit = prices[0], 0
        for p in prices[1:]:
            max_profit = max(max_profit, p - lowest)
            lowest = min(lowest, p)
        return max_profit
        