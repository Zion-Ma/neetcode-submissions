"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([intv.start for intv in intervals])
        end = sorted([intv.end for intv in intervals])
        s, e = 0, 0
        res, count, leng = 0, 0, start.__len__()
        while s < leng:
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(count, res)
        return res
        