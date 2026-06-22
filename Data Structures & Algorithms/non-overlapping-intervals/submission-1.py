class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0][1]
        count = 0
        for s, e in intervals[1:]:
            if s >= prev:
                prev = e
            else:
                count += 1
                prev = min(prev, e)
        return count