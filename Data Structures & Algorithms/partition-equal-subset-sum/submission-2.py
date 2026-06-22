class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        half = s // 2
        dp = [False] * (half + 1)
        dp[0] = True
        for n in nums:
            for t in range(half, n - 1, -1):
                dp[t] = dp[t] or dp[t - n]
        return dp[half]