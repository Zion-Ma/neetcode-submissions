class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        records = set(nums)
        ans = 0
        for n in nums:
            if n - 1 not in records:
                res = 1
                while n + 1 in records:
                    res += 1
                    n += 1
                ans = max(ans, res)
        return ans