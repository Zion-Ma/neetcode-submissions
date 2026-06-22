class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(i, curr_list, curr_sum):
            if curr_sum == target:
                ans.append(curr_list)
                return
            if not i < len(nums) or curr_sum > target:
                return
            backtrack(i, curr_list + [nums[i]], curr_sum + nums[i])
            backtrack(i + 1, curr_list, curr_sum)
        backtrack(0, [], 0)
        return ans
            