class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, ans = nums[0], nums[0]
        for n in nums[1:]:
            curr = max(curr + n, n)
            ans = max(curr, ans)
        return ans