class Solution:
    def jump(self, nums: List[int]) -> int:
        hop = 0
        curr_end = 0
        max_reach = 0
        for i, n in enumerate(nums):
            if i + n > max_reach:
                max_reach = i + n
            if i == curr_end:
                curr_end = max_reach
                hop += 1 if i < len(nums) - 1 else 0
        return hop