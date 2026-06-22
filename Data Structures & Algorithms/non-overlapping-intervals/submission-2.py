class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        prev = intervals[0][1]
        count = 0
        for intv in intervals[1:]:
            if intv[0] >= prev:
                prev = intv[1]
            else:
                prev = min(intv[1], prev)
                count += 1
        return count