class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s, e = 0, len(heights) - 1
        area = float("-inf")
        while s < e:
            curr = min(heights[s], heights[e]) * (e - s)
            area = max(area, curr)
            if heights[s] > heights[e]:
                e -= 1
            else:
                s += 1
        return area