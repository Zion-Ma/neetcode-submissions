class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        new = []
        for x, y in intervals:
            if new and x <= new[-1][1]:
                new[-1][1] = max(new[-1][1], y)
            else:
                new.append([x, y])
        return new