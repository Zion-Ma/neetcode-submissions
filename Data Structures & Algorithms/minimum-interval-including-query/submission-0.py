class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        pq = []
        res, i = dict(), 0
        for q in sorted(queries):
            if q in res:
                continue
            while i < len(intervals) and intervals[i][0] <= q:
                s, e = intervals[i]
                heapq.heappush(pq, (e - s + 1, e))
                i += 1
            while pq and pq[0][1] < q:
                heapq.heappop(pq)
            res[q] = pq[0][0] if pq else -1
        return [res[q] for q in queries]
        