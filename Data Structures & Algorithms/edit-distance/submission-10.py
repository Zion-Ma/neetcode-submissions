class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if n == 0:
            return m
        dp = defaultdict(int)
        def dfs(i: int, j: int) -> int:
            if i == m:
                return n - j
            if j == n:
                return m - i
            if (i, j) in dp:
                return dp[(i, j)]
            res = 0
            if word1[i] == word2[j]:
                res = dfs(i + 1, j + 1)
            else:
                res = 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))
            dp[(i, j)] = res
            return res
        return dfs(0, 0)