class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxreach = 0
        final = len(nums) - 1
        for i, n in enumerate(nums):
            if maxreach >= final:
                return True
            if maxreach < i:
                return False
            if (i + n) > maxreach:
                maxreach = i + n
        return True