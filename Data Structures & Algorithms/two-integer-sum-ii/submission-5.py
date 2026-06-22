class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            currTarget = target - numbers[left]
            if numbers[right] == currTarget:
                return [left + 1, right + 1]
            elif numbers[right] < currTarget:
                left += 1
            else:
                right -= 1
