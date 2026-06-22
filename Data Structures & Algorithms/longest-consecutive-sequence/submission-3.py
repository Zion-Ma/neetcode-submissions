class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        uniq = set(nums)
        for n in nums:
            if n - 1 not in uniq:
                step = 1
                while n + step in uniq:
                    step += 1
                longest = max(longest, step)
        return longest