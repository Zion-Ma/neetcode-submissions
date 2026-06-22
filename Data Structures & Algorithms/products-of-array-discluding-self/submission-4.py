class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leng, prod, suffix = nums.__len__(), [1], 1
        for i in range(1, leng):
            prod.append(nums[i - 1] * prod[i - 1])
        for i in range(leng - 1, -1, -1):
            prod[i] = prod[i] * suffix
            suffix *= nums[i]
        return prod
