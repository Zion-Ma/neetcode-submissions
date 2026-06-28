class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = dict()
        def dfs(i: int) -> bool:
            if i in dp:
                return dp[i]
            if i == 0:
                return True
            if i < 0:
                return False
            for word in wordDict:
                l = len(word)
                if i < l or s[i-l:i] != word:
                    continue
                if dfs(i - l):
                    dp[i] = True
                    return True
            dp[i] = False
            return False
        return dfs(len(s))
