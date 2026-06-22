"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals = sorted(intervals, key = lambda x:x.start)
        prevEnd = intervals[0].end
        for intv in intervals[1:]:
            if intv.start >= prevEnd:
                prevEnd = intv.end
            else:
                return False
        return True

