class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for n in nums:
            next_dp = defaultdict(int)
            for curr_sum, num in dp.items():
                next_dp[curr_sum + n] += num
                next_dp[curr_sum - n] += num
            dp = next_dp
        return dp[target]