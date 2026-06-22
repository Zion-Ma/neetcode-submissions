class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        for i in range(1, len(nums)):
            ans.append(ans[-1] * nums[i - 1])
        needMultiply = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = ans[i] * needMultiply
            needMultiply *= nums[i]
        return ans