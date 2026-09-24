class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_start, res_len = 0, 0
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                dp[i][j] = (
                    s[i] == s[j] and \
                    (j - i <= 2 or dp[i + 1][j - 1])
                )
                if dp[i][j] and (j - i + 1) > res_len:
                    res_start = i
                    res_len = j - i + 1
        return s[res_start:res_start + res_len]