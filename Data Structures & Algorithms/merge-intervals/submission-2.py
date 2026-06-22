class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start, end = intervals[0]
        res = []
        for intv in intervals:
            if intv[0] <= end:
                start = min(start, intv[0])
                end = max(end, intv[1])
            else:
                res.append([start, end])
                start, end = intv[0], intv[1]
        res.append([start, end])
        return res