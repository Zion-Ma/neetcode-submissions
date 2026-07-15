class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # if target in nums:
        #     return 1
        curr_sum = 0
        Min = 100001
        start = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            while start <= i and curr_sum >= target:
                Min = min(Min, i - start + 1)
                curr_sum -= nums[start]
                start += 1
        return Min if Min != 100001 else 0