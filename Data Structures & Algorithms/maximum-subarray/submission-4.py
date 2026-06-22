class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, ans = nums[0], nums[0]
        for i in range(1, len(nums)):
            curr = max(curr + nums[i], nums[i])
            ans = max(ans, curr)
        return ans
