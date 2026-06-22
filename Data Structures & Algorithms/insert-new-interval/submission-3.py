class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        ans = []
        # skipping and appending
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
        # merging
        # s, e = min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])
        # i += 1
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[1] = max(newInterval[1], intervals[i][1])
            newInterval[0] = min(newInterval[0], intervals[i][0])
            i += 1
        ans.append(newInterval)
        # getting everthing left
        if i < len(intervals):
            ans += intervals[i:]
        return ans
        