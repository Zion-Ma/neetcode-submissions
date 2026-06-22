class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weights = [-s for s in stones]
        heapq.heapify(weights)
        while len(weights) > 1:
            x = heapq.heappop(weights)
            y = heapq.heappop(weights)
            if x != y:
                heapq.heappush(weights, x - y)
        return abs(weights[0]) if weights else 0