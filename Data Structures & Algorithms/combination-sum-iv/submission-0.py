class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0:1}
        def dfs(remain: int) -> int:
            if remain in dp:
                return dp[remain]
            total = 0
            for n in nums:
                if n <= remain:
                    total += dfs(remain - n)
            dp[remain] = total
            return total
        return dfs(target)