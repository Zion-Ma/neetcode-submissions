class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n, suffix, ans = nums.__len__(), 1, [1]
        for i in range(1, n):
            ans.append(nums[i - 1] * ans[i - 1])
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        return ans