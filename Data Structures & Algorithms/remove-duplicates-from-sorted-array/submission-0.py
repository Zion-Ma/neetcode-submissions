class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        k = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                nums.pop(j)
            k += 1
            i += 1
        return k
