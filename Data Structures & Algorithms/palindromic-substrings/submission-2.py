class Solution:
    def countSubstrings(self, s: str) -> int:
        leng = s.__len__()
        if leng == 1:
            return 1
        def check(l: int, r: int) -> int:
            count = 0
            while l >= 0 and r < leng and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        ans = 0
        for i in range(leng):
            ans += check(i, i)
            ans += check(i, i + 1)
        return ans