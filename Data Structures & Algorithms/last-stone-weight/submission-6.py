class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        newStones = [-s for s in stones]
        heapq.heapify(newStones)
        while len(newStones) > 1:
            x = -heapq.heappop(newStones)
            y = -heapq.heappop(newStones)
            remain = y - x
            if remain != 0:
                heapq.heappush(newStones, remain)
        return -newStones[0] if len(newStones) == 1 else 0