class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        for p in points:
            x, y = p[0], p[1]
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(result, (-dist, [x, y]))
            if len(result) > k:
                heapq.heappop(result)
        return [element[1] for element in result]
