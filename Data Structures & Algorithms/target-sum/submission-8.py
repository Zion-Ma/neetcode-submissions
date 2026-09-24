class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for n in nums:
            new_dp = defaultdict(int)
            # new_dp[0] = 1
            for key in dp.keys():
                new_dp[key + n] += dp[key]
                new_dp[key - n] += dp[key]
            dp = new_dp
        return dp[target]