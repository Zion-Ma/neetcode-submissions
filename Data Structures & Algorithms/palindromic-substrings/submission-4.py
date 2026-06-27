class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPali(l: int, r: int) -> int:
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res
        ans = 0
        for i in range(len(s)):
            ans += countPali(i, i)
            ans += countPali(i, i + 1)
        return ans