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
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged_list.append(list1[i])
                i += 1
            else:
                merged_list.append(list2[j])
                j += 1
        merged_list += list1[i:] if i < len(list1) else list2[j:]
        return merged_list