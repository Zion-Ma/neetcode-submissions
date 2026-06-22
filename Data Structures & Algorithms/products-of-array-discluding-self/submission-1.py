class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n, prod, suffix = len(nums), [1], 1
        for i in range(1, n):
            prod.append(prod[i-1]*nums[i-1])
        for i in range(n-1, -1, -1):
            prod[i] = prod[i] * suffix
            suffix = suffix * nums[i]
        return prod
        