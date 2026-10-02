class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max, curr_min = 0, 0
        global_max, global_min = nums[0], nums[0]
        total = 0
        for n in nums:
            curr_max = max(curr_max + n, n)
            curr_min = min(curr_min + n, n)
            global_max = max(global_max, curr_max)
            global_min = min(global_min, curr_min)
            total += n
        if global_max < 0:
            return global_max
        return max(global_max, total - global_min)