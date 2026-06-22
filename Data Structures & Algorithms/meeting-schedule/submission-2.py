"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        intervals = sorted(intervals, key = lambda x:x.start)
        prev = intervals[0].end
        for intv in intervals[1:]:
            if intv.start < prev:
                return False
            prev = intv.end
        return True