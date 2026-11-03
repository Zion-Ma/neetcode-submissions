class Solution:
    def longestPalindrome(self, s: str) -> str:
        # build the palindrome table
        n = len(s)
        palin_table = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                palin_table[i][j] = (s[i] == s[j] and (j - i <= 2 or palin_table[i + 1][j - 1]))
                
        # find the max
        global_max = 0
        start, end = 0, 0
        for i in range(n):
            for j in range(i, n):
                if palin_table[i][j] and j - i + 1 > global_max:
                    global_max = j - i + 1
                    start, end = i, j + 1
        return s[start:end]