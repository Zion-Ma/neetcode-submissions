class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_max = 0
        for i, n in enumerate(nums):
            if i > curr_max:
                return False
            if curr_max >= len(nums) - 1:
                return True
            curr_max = max(curr_max, i + nums[i])