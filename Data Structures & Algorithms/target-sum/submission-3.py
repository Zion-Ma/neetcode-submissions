class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp: list[dict[int, int]] = [{} for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(n):
            for total, count in dp[i].items():
                if total + nums[i] not in dp[i + 1]:
                    dp[i + 1][total + nums[i]] = 0
                if total - nums[i] not in dp[i + 1]:
                    dp[i + 1][total - nums[i]] = 0
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count
        result = dp[n].get(target, 0)
        return result
