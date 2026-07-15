class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        if len(nums) == 2:
            return [min(nums), max(nums)]
        m = len(nums) // 2
        left, right = self.sortArray(nums[0:m]), self.sortArray(nums[m:])
        new = self.merge(left, right)
        return new

    def merge(self, list1: list[int], list2: list[int]) -> list[int]:
        merged_list = []
        while list1 and list2:
            if list1[0] < list2[0]:
                merged_list.append(list1.pop(0))
            else:
                merged_list.append(list2.pop(0))
        merged_list += list1 if list1 else list2
        return merged_list