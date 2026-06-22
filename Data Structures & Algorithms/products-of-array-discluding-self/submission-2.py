class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leng, prod, ans = nums.__len__(), 1, [1]
        for i in range(1, leng):
            ans.append(nums[i - 1] * ans[i - 1])
        for i in range(leng - 1, -1, -1):
            ans[i] = ans[i] * prod
            prod = prod * nums[i]
        return ans
