class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = dict()
        for i in range(len(nums)):
            curr_comp = target - nums[i]
            if curr_comp in comp:
                return [comp[curr_comp], i]
            else:
                comp[nums[i]] = i
        return [] 