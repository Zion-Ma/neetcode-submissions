class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals = sorted(intervals, key = lambda x:x[0])
        for intv in intervals:
            if not ans or intv[0] > ans[-1][1]:
                ans.append(intv)
            else:
                ans[-1][1] = max(ans[-1][1], intv[1])
        return ans
        