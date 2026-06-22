class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxreach = 0
        l = len(nums) - 1
        for i, n in enumerate(nums):
            if maxreach >= l:
                return True
            if i > maxreach:
                return False
            if (i + n) > maxreach:
                maxreach = i + n
        return True