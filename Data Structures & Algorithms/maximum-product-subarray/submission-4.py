class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        Min, Max = 1, 1
        ans = max(nums)
        for n in nums:
            temp = n * Max
            Max = max(temp, Min * n, n)
            Min = min(temp, Min * n, n)
            ans = max(Max, ans)
        return ans
            