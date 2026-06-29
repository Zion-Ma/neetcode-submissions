class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr = nums[0]
        for n in nums[1:]:
            curr = max(n, curr + n)
            res = max(res, curr)
        return res