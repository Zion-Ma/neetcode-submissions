class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = nums.__len__()
        def dfs(idx, curr):
            if idx == n:
                res.append(curr.copy())
                return
            curr.append(nums[idx])
            dfs(idx + 1, curr)
            curr.pop()
            while idx + 1 < n and nums[idx] == nums[idx + 1]:
                idx += 1
            dfs(idx + 1, curr)
        dfs(0, [])
        return res
        