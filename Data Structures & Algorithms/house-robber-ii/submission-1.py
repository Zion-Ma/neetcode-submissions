class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def get_max(nums_curr):
            prev1, prev2 = nums_curr[0], 0
            for i in range(1, len(nums_curr)):
                curr = max(prev1, prev2 + nums_curr[i])
                prev1, prev2 = curr, prev1
            return prev1
        return max(get_max(nums[:-1]), get_max(nums[1:]))