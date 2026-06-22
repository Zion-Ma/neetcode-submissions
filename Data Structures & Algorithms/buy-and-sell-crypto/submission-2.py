class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 101
        m = 0
        for p in prices:
            m = max(m, p - low)
            low = min(low, p)
        return m
        