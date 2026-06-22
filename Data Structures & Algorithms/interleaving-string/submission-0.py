class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        if n2 > n1:
            s1, s2 = s2, s1
            n1, n2 = n2, n1
        dp = [False] * (n1 + 1)
        dp[-1] = True
        for i in range(n2, -1, -1):
            nextDP = [False] * (n1 + 1)
            nextDP[-1] = True
            for j in range(n1, -1, -1):
                if i < n2 and s2[i] == s3[i + j] and dp[j]:
                    nextDP[j] = True
                if j < n1 and s1[j] == s3[i + j] and nextDP[j + 1]:
                    nextDP[j] = True
            dp = nextDP
        return dp[0]
        