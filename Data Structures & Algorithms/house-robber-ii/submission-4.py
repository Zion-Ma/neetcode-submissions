class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def subRob(subNums: list) -> int:
            prev1, prev2 = subNums[0], 0
            for i in range(1, len(subNums)):
                curr = max(prev2 + subNums[i], prev1)
                prev1, prev2 = curr, prev1
            return prev1
        return max(subRob(nums[:-1]), subRob(nums[1:]))