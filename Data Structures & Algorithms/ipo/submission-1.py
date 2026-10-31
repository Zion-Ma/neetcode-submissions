class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        sorted_index = [i for i in range(len(profits))]
        sorted_index.sort(key = lambda i:capital[i])
        max_heap = []
        i = 0
        for _ in range(k):
            while i < len(profits) and capital[sorted_index[i]] <= w:
                heapq.heappush(max_heap, -profits[sorted_index[i]])
                i += 1
            if not max_heap:
                break
            w += -heapq.heappop(max_heap)
        return w