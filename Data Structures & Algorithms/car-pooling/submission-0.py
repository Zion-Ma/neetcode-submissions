class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[1])
        drop_heap = []
        for n, f, t in trips:
            while drop_heap and drop_heap[0][0] <= f:
                _, count = heapq.heappop(drop_heap)
                capacity += count
            capacity -= n
            if capacity < 0:
                return False
            heapq.heappush(drop_heap, (t, n))
        return True