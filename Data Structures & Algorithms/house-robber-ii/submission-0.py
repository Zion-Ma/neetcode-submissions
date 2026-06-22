class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def getmax(num_list):
            prev2, prev1 = 0, num_list[0]
            for n in num_list[1:]:
                curr = max(prev1, prev2 + n)
                prev2, prev1 = prev1, curr
            return prev1
        return max(getmax(nums[1:]), getmax(nums[:-1]))