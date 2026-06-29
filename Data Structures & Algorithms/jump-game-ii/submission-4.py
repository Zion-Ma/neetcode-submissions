class Solution:
    def jump(self, nums: List[int]) -> int:
        hop = 0
        l, r, farthest = 0, 0, 0
        while farthest < len(nums) - 1:
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l, r = r + 1, farthest
            hop += 1
        return hop