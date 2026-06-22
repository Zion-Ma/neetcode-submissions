class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        def count_pal(l, r):
            count = 0 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count
        ans = 0
        for i in range(len(s)):
            ans += count_pal(i, i)
            ans += count_pal(i, i + 1)
        return ans
        