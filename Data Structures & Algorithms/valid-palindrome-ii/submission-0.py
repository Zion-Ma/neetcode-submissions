class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPali(i: int, j: int, no_remove: bool) -> bool:
            if i >= j:
                return True
            if s[i] == s[j]:
                return isPali(i + 1, j - 1, no_remove)
            if not no_remove:
                return False
            return isPali(i + 1, j, False) or isPali(i, j - 1, False)
        return isPali(0, len(s) - 1, True)