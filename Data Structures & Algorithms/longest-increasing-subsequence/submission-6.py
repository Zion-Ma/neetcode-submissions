class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                result[i] = max(result[i], 1 + result[j])
        return max(result)