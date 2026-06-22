class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        ans, j = 0, 0
        for i, ch in enumerate(s):
            if ch in seen and seen[ch] >= j:
                j = seen[ch] + 1
            seen[ch] = i
            ans = max(ans, i - j + 1)
        return ans