class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf") for _ in range(n)]
        prices[src] = 0
        for _ in range(k + 1):
            new_prices = prices.copy()
            for u, v, p in flights:
                new_prices[v] = min(new_prices[v], prices[u] + p)
            if prices[dst] != float("inf") and new_prices == prices:
                return prices[dst]
            prices = new_prices
        return -1 if prices[dst] == float("inf") else prices[dst]