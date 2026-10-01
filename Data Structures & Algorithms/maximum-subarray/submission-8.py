class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runningMax, globalMax = nums[0], nums[0]
        for n in nums[1:]:
            runningMax = max(runningMax + n, n)
            globalMax = max(runningMax, globalMax)
        return globalMax