class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0][1]
        count = 0
        for intv in intervals[1:]:
            if intv[0]>= prev:
                prev = intv[1]
            else:
                count += 1
                prev = min(prev, intv[1])
        return count
        