class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        coins = dict() # (index<int>, buying <bool>) : profit <int>
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in coins:
                return coins[(i, buying)]
            cooldown = dfs(i + 1, buying)
            today = -1
            if buying: # we can buy
                today = dfs(i + 1, not buying) - prices[i]
            else:
                today = dfs(i + 2, not buying) + prices[i]
            coins[(i, buying)] = max(today, cooldown)
            return coins[(i, buying)]
        return dfs(0, True)