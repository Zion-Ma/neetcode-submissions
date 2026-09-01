class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for n in nums:
            if n - 1 in nums:
                continue
            curr = n
            count = 1
            while curr + 1 in nums:
                count += 1
                curr += 1
            ans = max(count, ans)
        return ans