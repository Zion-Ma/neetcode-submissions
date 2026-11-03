class Solution:
    def longestPalindrome(self, s: str) -> str:
        # build the palindrome table
        n = len(s)
        palin_table = [[False for _ in range(n)] for _ in range(n)]
        global_max = 0
        start = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if (s[i] == s[j] and (j - i <= 2 or palin_table[i + 1][j - 1])):
                    palin_table[i][j] = True
                    if j - i + 1 > global_max:
                        global_max = j - i + 1
                        start = i
        return s[start:start + global_max]