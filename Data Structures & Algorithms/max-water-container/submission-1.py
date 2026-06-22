class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s, e = 0, len(heights) - 1
        area = float("-inf")
        while s <= e:
            curr = min(heights[s], heights[e]) * (e - s)
            area = max(curr, area)
            if heights[e] > heights[s]:
                s += 1
            else:
                e -= 1
        return area

        