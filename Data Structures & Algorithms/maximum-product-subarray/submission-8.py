class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        Max, Min = 1, 1
        ans = nums[0]
        for n in nums:
            temp = Max
            Max = max(n, Max * n, Min * n)
            Min = min(n, temp * n, Min * n)
            ans = max(Max, ans)
        return ans