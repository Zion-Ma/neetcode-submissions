class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        pivot = nums[len(nums) // 2]
        left, mid, right = [], [], []
        for i in range(len(nums)):
            if nums[i] > pivot:
                right.append(nums[i])
            elif nums[i] < pivot:
                left.append(nums[i])
            else:
                mid.append(nums[i])
        left, right = self.sortArray(left), self.sortArray(right)
        return left + mid + right
