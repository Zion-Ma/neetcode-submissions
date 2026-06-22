class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_length = len(set(nums))
        return set_length < len(nums) 