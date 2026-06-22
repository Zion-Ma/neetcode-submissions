class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area, l, r = -1, 0, heights.__len__() - 1
        while l < r:
            base = r - l
            max_area = max(max_area, min(heights[l], heights[r]) * base)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area
