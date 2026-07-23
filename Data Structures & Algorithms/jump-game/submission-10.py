class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, num in enumerate(nums):
            if i > max_reach:
                return False
            if max_reach >= len(nums) - 1:
                return True
            max_reach = max(max_reach, i + num)
        return True