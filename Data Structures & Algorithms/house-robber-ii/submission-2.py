class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dp(seq):
            prev2, prev1 = 0, seq[0]
            for i in range(1, len(seq)):
                curr = max(prev2 + seq[i], prev1)
                prev2, prev1 = prev1, curr
            return prev1
        return max(dp(nums[:-1]), dp(nums[1:]))