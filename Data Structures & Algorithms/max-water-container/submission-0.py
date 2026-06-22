class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        l = 0
        r = height.__len__() - 1
        while l < r:
            maxA = max(maxA, (r - l) * min(height[l], height[r]))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxA