class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        dp = dict()
        def dfs(i: int, j: int) -> int:
            if j == n:
                return 1
            if i == m:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            res = 0
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            res += dfs(i + 1, j)
            dp[(i, j)] = res
            return res
        return dfs(0, 0)