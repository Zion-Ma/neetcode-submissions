class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2
        dp: dict[int, dict] = dict()

        def dfs(i: int, curr_sum: int) -> bool:
            if curr_sum == target:
                return True
            if i >= len(nums):
                return False
            if i in dp and curr_sum in dp[i]:
                return dp[i][curr_sum]
            #TODO: update dp
            result = dfs(i + 1, curr_sum) or dfs(i + 1, curr_sum + nums[i])
            if i not in dp:
                dp[i] = dict()
            dp[i][curr_sum] = result
            return result

        return dfs(0, 0)
            