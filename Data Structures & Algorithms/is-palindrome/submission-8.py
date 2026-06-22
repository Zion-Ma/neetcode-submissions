class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            left, right = s[l], s[r]
            if not left.isalpha() and not left.isdigit():
                l += 1
            elif not right.isalpha() and not right.isdigit():
                r -= 1
            else:
                if left.lower() != right.lower():
                    return False
                l += 1
                r -= 1
        return True