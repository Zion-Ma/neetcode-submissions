class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, nums[0]
        for i in range(1, len(nums)):
            curr = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = curr
        return max(prev2, prev1)