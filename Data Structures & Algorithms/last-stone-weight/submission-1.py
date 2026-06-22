class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weight = []
        for s in stones:
            weight.append(-s)
        heapq.heapify(weight)
        while len(weight) > 1:
            x = -heapq.heappop(weight)
            y = -heapq.heappop(weight)
            if x != y:
                new = -abs(x - y)
                heapq.heappush(weight, new)
        return -weight[0] if weight else 0

