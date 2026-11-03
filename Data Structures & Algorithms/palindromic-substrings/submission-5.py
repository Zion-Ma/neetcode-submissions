class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        palin_table = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if (s[i] == s[j] and (j - i + 1 <= 2 or palin_table[i + 1][j - 1])):
                    palin_table[i][j] = True
                    ans += 1
        return ans