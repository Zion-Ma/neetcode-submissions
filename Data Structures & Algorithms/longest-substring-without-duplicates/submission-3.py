class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, m = 0, 0
        position = dict()
        for i, item in enumerate(s):
            if item in position and start <= position[item]:
                start = position[item] + 1
            else:
                m = max(m, i - start + 1)
            position[item] = i
        return m