class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = heights.__len__()
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, h2 = stack.pop()
                curr_area = (i - idx) * h2
                max_area = max(max_area, curr_area)
                start = idx
            stack.append((start, h))
        for idx, h in stack:
            max_area = max(max_area, h * (n - idx))
        return max_area

