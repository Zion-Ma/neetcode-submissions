class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        Min, Max = 1, 1
        result = float("-inf")
        for n in nums:
            temp = Max
            Max = max(temp * n, Min * n, n)
            Min = min(temp * n, Min * n, n)
            result = max(result, Max)
        return result