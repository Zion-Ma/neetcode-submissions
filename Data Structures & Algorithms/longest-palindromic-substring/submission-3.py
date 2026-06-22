class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        def check(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        m = 0
        pos = -1
        for i in range(len(s)):
            even = check(i, i + 1)
            odd = check(i, i)
            curr_max = max(odd, even)
            if curr_max > m:
                m = curr_max
                pos = i
        if m % 2:
            return s[(pos - m // 2):(pos + m // 2 + 1)]
        else:
            return s[(pos - m // 2 + 1):(pos + m // 2 + 1)]