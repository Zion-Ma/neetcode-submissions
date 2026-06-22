class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        def check(l, r):
            while l >= 0 and r < len(s) and s[r] == s[l]:
                l -= 1
                r += 1
            return r - l - 1

        maximum = float("-inf")
        center = 0
        for i in range(len(s)):
            odd = check(i - 1, i + 1)
            even = check(i, i + 1)
            curr = max(odd, even)
            if curr > maximum:
                maximum = curr
                center = i
        if maximum % 2:
            return s[center - maximum // 2:center + maximum // 2 + 1]
        else:
            return s[center - maximum // 2 + 1:center + maximum // 2 + 1]


