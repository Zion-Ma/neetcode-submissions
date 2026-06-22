"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
"""
sort start and end

"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start, end = [], []
        for intv in intervals:
            start.append(intv.start)
            end.append(intv.end)
        start.sort()
        end.sort()
        i, j, n = 0, 0, len(intervals)
        count, res = 0, 0
        while i < n:
            if start[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(res, count)
        return res
