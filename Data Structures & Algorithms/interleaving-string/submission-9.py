class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        if n > m:
            s1, s2 = s2, s1
            m, n = n, m
        print(n >= m)
        dp = [False] * (n + 1)
        dp[-1] = True
        for i in range(m, -1, -1):
            nextDP = [False] * (n + 1)
            nextDP[-1] = True
            for j in range(n, -1, -1):
                if i < m and s1[i] == s3[i + j] and dp[j]:
                    nextDP[j] = True
                if j < n and s2[j] == s3[i + j] and nextDP[j + 1]:
                    nextDP[j] = True
                # nextDP[j] = cond1 or cond2
            dp = nextDP
        return dp[0]
                