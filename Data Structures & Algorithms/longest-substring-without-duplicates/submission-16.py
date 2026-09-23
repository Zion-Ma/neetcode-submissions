class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        pos = defaultdict(int)
        start = 0
        for i in range(len(s)):
            ch = s[i]
            if ch in pos and pos[ch] >= start:
                start = pos[ch] + 1
            maxLen = max(maxLen, i - start + 1)
            pos[ch] = i
        return maxLen
            