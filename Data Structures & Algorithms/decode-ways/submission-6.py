class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i: int) -> int:
            if i == len(s):
                return 1
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0
            one_step = dfs(i + 1)
            two_step = 0
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in "0123456")):
                two_step = dfs(i + 2)
            dp[i] = one_step + two_step
            return dp[i]
        
        dp = dict()
        return dfs(0)
            