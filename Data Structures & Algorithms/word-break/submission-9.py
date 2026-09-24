class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {len(s):True}
        def dfs(i: int) -> bool:
            if i in dp:
                return dp[i]
            for w in wordDict:
                j = len(w)
                if i + j <= len(s) and s[i:i + j] == w:
                    if dfs(i + j):
                        dp[i] = True
                        return True
            dp[i] = False
            return False
        return dfs(0)
