class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if prices.__len__() == 1:
        #     return 0
        max_profit = 0
        purchase_price = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, (prices[i] - purchase_price))
            purchase_price = min(purchase_price, prices[i])
        return max_profit