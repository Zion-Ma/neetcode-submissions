class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        def partial_len(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        start, m = 0, 0
        for i in range(len(s)):
            odd = partial_len(i - 1, i + 1)
            even = partial_len(i, i + 1)
            curr = max(odd, even)
            if curr > m:
                m = curr
                start = i
        if m % 2:
            st, e = start - m // 2, start + m // 2 + 1
        else:
            st, e = start - m // 2 + 1, start + m // 2 + 1
        return s[st:e]