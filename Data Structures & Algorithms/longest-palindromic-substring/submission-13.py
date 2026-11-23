class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        start, length = 0, 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1])
                if dp[i][j] and j - i + 1 > length:
                    start = i
                    length = j - i + 1
        return s[start:start+length]
