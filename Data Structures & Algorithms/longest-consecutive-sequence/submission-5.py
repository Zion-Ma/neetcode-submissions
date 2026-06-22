class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        res = 0
        for n in nums:
            if not dp[n]:
                dp[n] = dp[n - 1] + dp[n + 1] + 1
                dp[n - dp[n - 1]] = dp[n]
                dp[n + dp[n + 1]] = dp[n]
                res = max(dp[n], res)
        return res
