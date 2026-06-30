class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        ans = 0
        for x, y in intervals[1:]:
            if x >= prevEnd:
                prevEnd = y
            else:
                prevEnd = min(prevEnd, y)
                ans += 1
        return ans