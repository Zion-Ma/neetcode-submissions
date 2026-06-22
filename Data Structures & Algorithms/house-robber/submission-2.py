class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, nums[0]
        for i in range(1, len(nums)):
            curr = max(prev1, prev2 + nums[i])
            prev1, prev2 = curr, prev1
        return prev1
