class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        # dp = [[0] * n1 for _ in range(n2)]
        dp = {}
        def dfs(i, j, k):
            if k == n3:
                return i == n1 and j == n2
            if (i, j) in dp:
                return dp[(i, j)]
            res = False
            if i < n1 and s1[i] == s3[k]:
                res = dfs(i + 1, j, k + 1)
            if not res and j < n2 and s2[j] == s3[k]:
                res = dfs(i, j + 1, k + 1)
            dp[(i, j)] = res
            return res
        return dfs(0, 0, 0)