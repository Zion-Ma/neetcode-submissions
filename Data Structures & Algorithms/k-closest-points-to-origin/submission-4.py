class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [(math.sqrt(x ** 2 + y ** 2), i) for i, (x, y) in enumerate(points)]
        heapq.heapify(dist)
        ans = []
        count = 0
        while count < k:
            item = heapq.heappop(dist)
            ans.append(points[item[1]])
            count += 1
        return ans
        