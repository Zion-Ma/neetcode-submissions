class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        s, e = 0, len(heights) - 1
        while s < e:
            area = min(heights[s], heights[e]) * (e - s)
            ans = max(ans, area)
            if heights[s] > heights[e]:
                e -= 1
            else:
                s += 1
        return ans