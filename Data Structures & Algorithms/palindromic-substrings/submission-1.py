class Solution:
    def countSubstrings(self, s: str) -> int:
        if s.__len__() == 1:
            return 1
        def check(l: int, r: int) -> int:
            count = 0
            while l >= 0 and r < s.__len__() and s[r] == s[l]:
                count += 1
                l -= 1
                r += 1
            return count

        ans = 0
        for i in range(s.__len__()):
            ans += check(i, i)
            ans += check(i, i + 1)
        return ans