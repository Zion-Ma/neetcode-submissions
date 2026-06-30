"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        ans = 0
        if not intervals:
            return ans
        intervals = sorted(intervals, key = lambda x:x.start)
        rooms = 0
        max_rooms = 0
        minH = []
        for intv in intervals:
            if not minH:
                heapq.heappush(minH, intv.end)
                rooms += 1
            else:
                while minH and intv.start >= minH[0]:
                    heapq.heappop(minH)
                    rooms -= 1
                heapq.heappush(minH, intv.end)
                rooms += 1
            max_rooms = max(max_rooms, rooms)
        return max_rooms

                    
                
        
        