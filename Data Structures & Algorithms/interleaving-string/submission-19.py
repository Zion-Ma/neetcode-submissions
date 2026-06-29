class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, k = len(s1), len(s2), len(s3)
        if (m + n) != k:
            return False
        dp = defaultdict(bool)
        def dfs(i: int, j: int) -> bool:
            if (i + j) == k:
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            res = False
            if i < m and s3[i + j] == s1[i]:
                res = dfs(i + 1, j)
            if j < n and s3[i + j] == s2[j]:
                res |= dfs(i, j + 1)
            dp[(i, j)] = res
            return res
        return dfs(0, 0)