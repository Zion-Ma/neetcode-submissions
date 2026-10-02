class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max, cur_min = 0, 0
        global_max, global_min = nums[0], nums[0]
        total = 0
        for n in nums:
            cur_max = max(cur_max + n, n)
            cur_min = min(cur_min + n, n)
            global_max = max(cur_max, global_max)
            global_min = min(cur_min, global_min)
            total += n
        if global_max < 0:
            return global_max
        return max(global_max, total - global_min)
