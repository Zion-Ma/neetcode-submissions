class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        n, count = len(intervals), 1
        for intv in intervals[1:]:
            if intv[0] >= prevEnd:
                prevEnd = intv[1]
                count += 1
            else:
                prevEnd = min(prevEnd, intv[1])
                # count += 1
        return n - count