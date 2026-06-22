class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return s
        def check(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        max_len, center = 0, -1
        for i in range(len(s)):
            odd = check(i - 1, i + 1)
            even = check(i, i + 1)
            curr = max(odd, even)
            if curr > max_len:
                max_len = curr
                center = i
        # odd
        if max_len % 2:
            st, e = center - max_len // 2, center + max_len // 2 + 1
        else:
            st, e = center - max_len // 2 + 1, center + max_len // 2 + 1
        return s[st:e]