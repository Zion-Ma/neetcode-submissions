class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(l: int , r: int) -> int:
            if l > r:
                return -1
            mid = l + (r - l) // 2
            if nums[mid] > target:
                return binary(l, mid - 1)
            elif nums[mid] < target:
                return binary(mid + 1, r)
            else:
                return mid
        return binary(0, len(nums) - 1)
        
