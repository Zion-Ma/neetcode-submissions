class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for p in points:
            curr_dist = math.sqrt(pow(p[0], 2) + pow(p[1], 2))
            heapq.heappush(dist, (-curr_dist, p))
            print("before",dist)
            if len(dist) > k:
                heapq.heappop(dist)
            print("after",dist)
        return [d[1] for d in dist]
        