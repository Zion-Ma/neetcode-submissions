class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        position = dict()
        window_last = 0
        max_len = 0
        for i, ch in enumerate(s):
            if ch in position and position[ch] >= window_last:
                window_last = position[ch] + 1
            max_len = max(max_len, i - window_last + 1)
            position[ch] = i
        return max_len
