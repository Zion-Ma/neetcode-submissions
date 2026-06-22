class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = curr = nums[0]
        for n in nums[1:]:
            curr = max(curr + n, n)
            maxsum = max(maxsum, curr)
        return maxsum