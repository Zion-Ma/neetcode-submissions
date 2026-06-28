class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {len(s):True}
        def dfs(i: int) -> bool:
            if i in dp:
                return dp[i]
            if i == len(s):
                return True
            for w in wordDict:
                l = len(w)
                if i + l <= len(s) and s[i:i + l] == w:
                    if dfs(i + l):
                        dp[i] = True
                        return True
            dp[i] = False
            return False
        return dfs(0)
            