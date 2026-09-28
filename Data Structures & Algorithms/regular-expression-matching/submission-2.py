class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = dict()
        def dfs(i: int, j: int) -> bool:
            if j == n:
                return i == m
            if (i, j) in dp:
                return dp[(i, j)]
            match = i < m and (p[j] == '.' or s[i] == p[j])
            if j + 1 < n and p[j + 1] == '*':
                dp[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
            else:
                dp[(i, j)] = match and dfs(i + 1, j + 1)
            return dp[(i, j)]
        return dfs(0, 0)
            