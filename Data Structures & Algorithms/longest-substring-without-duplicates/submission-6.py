class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen, start, ans = dict(), 0, 0
        for i, ch in enumerate(s):
            if ch in seen and start <= seen[ch]: 
                start = seen[ch] + 1
            ans = max(ans, i - start + 1)
            seen[ch] = i
        return ans