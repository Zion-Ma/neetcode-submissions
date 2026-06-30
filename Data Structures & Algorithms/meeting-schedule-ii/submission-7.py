"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intervals = sorted(intervals, key = lambda x:x.start)
        start = sorted([intv.start for intv in intervals])
        end = sorted([intv.end for intv in intervals])
        count, max_count = 0, 0
        s, e = 0, 0
        while s < len(start):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            max_count = max(max_count, count)
        return max_count