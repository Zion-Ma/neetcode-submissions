from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = defaultdict(int)
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in numdict.keys():
                return [numdict[comp], i]
            else:
                numdict[nums[i]] = i


        