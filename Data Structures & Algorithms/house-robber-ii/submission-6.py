class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def subRob(target: list[int]) -> int:
            prev2, prev1 = 0, target[0]
            for i in range(1, len(target)):
                curr = max(prev2 + target[i], prev1)
                prev2, prev1 = prev1, curr
            return prev1
        return max(subRob(nums[:-1]), subRob(nums[1:]))