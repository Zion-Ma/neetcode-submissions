class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [nums[0]]
        suffix = [nums[-1]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] * prefix[-1])
            suffix.insert(0, suffix[0] * nums[len(nums) - 1 - i])
        # prefix.pop(0)
        # suffix.pop(0)
        final = [suffix[1]]
        for i in range(1, len(nums) - 1):
            final.append(prefix[i - 1] * suffix[i + 1])
        final.append(prefix[-2])
        return final
        