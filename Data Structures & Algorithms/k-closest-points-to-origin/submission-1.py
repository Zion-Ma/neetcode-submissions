class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        ans = []
        for i, p in enumerate(points):
            curr_dist = math.sqrt(pow(p[0], 2) + pow(p[1], 2))
            heapq.heappush(dist, (-curr_dist, i, p))
            if len(dist) > k:
                heapq.heappop(dist)
        while k > 0:
            ans.append(heapq.heappop(dist)[2])
            k -= 1
        return ans