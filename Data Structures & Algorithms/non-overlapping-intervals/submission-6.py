class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        ans = 0
        for i in range(1, len(intervals)):
            x, y = intervals[i]
            if x >= prevEnd:
                prevEnd = y
            else:
                prevEnd = min(prevEnd, y)
                ans += 1
        return ans