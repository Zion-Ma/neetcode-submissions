class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, m = 0, 0
        d = dict()
        for i, c in enumerate(s):
            if c in d and start <= d[c]:
                start = d[c] + 1
            else:
                m = max(m, i - start + 1)
            d[c] = i
        return m


        
        