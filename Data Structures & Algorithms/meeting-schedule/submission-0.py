"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        ordered = sorted(intervals, key = lambda x:x.start)
        prev = -1
        for intv in ordered:
            if intv.start < prev:
                return False
            prev = intv.end
        return True 
