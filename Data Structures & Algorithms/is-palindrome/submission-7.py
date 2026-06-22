class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, s.__len__() - 1
        while l < r:
            lc, rc = s[l], s[r]
            if not lc.isalpha() and not lc.isdigit():
                l += 1
            elif not rc.isalpha() and not rc.isdigit():
                r -= 1
            else:
                if lc.lower() != rc.lower():
                    return False
                else:
                    l += 1
                    r -= 1
        return True