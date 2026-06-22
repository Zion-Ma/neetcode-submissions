class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf") if i != src else 0 for i in range(n)]
        for i in range(k + 1):
            temp = prices.copy()
            for x, y, p in flights:
                temp[y] = min(temp[y], prices[x] + p)
            if prices[dst] != float("inf") and temp == prices:
                return prices[dst]
            prices = temp
        return prices[dst] if prices[dst] != float("inf") else -1


        