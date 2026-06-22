class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()
        for i, n in enumerate(nums):
            diff = target - n
            if diff in records:
                return [records[diff], i]
            records[n] = i 