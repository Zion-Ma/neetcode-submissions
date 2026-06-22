class Solution:
    def countSubstrings(self, s: str) -> int:
        def count(l, r):
            n = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                n += 1
                l -= 1
                r += 1
            return n
        ans = 0
        for i in range(len(s)):
            ans += count(i, i)
            ans += count(i, i + 1)
        return ans