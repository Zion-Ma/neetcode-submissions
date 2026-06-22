class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for intv in intervals[1:]:
            if intv[0] > ans[-1][1]:
                ans.append(intv)
            else:
                ans[-1][1] = max(ans[-1][1], intv[1])
        return ans