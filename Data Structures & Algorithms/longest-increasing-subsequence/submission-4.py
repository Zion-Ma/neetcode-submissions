class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                # using Max to avoid number that has been represented by lager numbers
                if nums[j] >= nums[i]:
                    continue
                dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

            