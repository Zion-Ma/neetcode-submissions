class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        Min, Max = nums[0], nums[0]
        ans = nums[0]
        for n in nums[1:]:
            result1 = Min * n
            result2 = Max * n
            Max = max(result1, result2, n)
            Min = min(result1, result2, n)
            ans = max(Max, ans)
        return ans
            