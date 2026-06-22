class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        def backtrack(i):
            if i >= len(nums):
                # save the current subset's copy, subset will be modified
                ans.append(subset.copy())
                return
            backtrack(i + 1)
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
        backtrack(0)
        return ans