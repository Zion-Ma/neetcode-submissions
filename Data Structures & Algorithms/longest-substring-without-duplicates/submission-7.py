class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = dict()
        start = 0
        ans = 0
        for i, ch in enumerate(s):
            if ch in pos and start <= pos[ch]:
                start = pos[ch] + 1
            else:
                ans = max(ans, i - start + 1)
            pos[ch] = i
        return ans

        