class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = [-s for s in stones]
        heapq.heapify(stones_heap)
        while len(stones_heap) > 1:
            s1 = heapq.heappop(stones_heap)
            s2 = heapq.heappop(stones_heap)
            if s1 != s2:
                heapq.heappush(stones_heap, -abs(s1 - s2))
        return -stones_heap[0] if stones_heap else 0