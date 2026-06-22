class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 101
        profit = 0
        for p in prices:
            profit = max(p - lowest, profit)
            lowest = min(lowest, p)
        return profit