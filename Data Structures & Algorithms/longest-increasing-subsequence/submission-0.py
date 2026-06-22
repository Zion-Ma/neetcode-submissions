class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        leng = len(nums)
        dp = [1] * leng
        for i in range(leng - 1, -1, -1):
            for j in range(i + 1, leng):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
        