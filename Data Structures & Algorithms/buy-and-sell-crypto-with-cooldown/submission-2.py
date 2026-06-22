class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, buy_2 = 0, 0, 0
        for i in range(len(prices) - 1, -1, -1):
            new_buy = max(buy, sell - prices[i])
            new_sell = max(sell, buy_2 + prices[i])
            buy_2 = buy
            buy, sell = new_buy, new_sell
        return buy