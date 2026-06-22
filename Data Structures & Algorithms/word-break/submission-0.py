class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        leng = len(s)
        dp = [False] * (leng + 1)
        dp[-1] = True
        for i in range(leng - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= leng and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
        