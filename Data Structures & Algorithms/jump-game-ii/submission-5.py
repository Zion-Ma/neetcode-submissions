class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        l, r, farthest = 0, 0, 0
        while r < len(nums) - 1:
            print(r)
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            count += 1
            l = r + 1
            r = farthest
        return count