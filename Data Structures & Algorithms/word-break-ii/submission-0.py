class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(i: int) -> list:
            if i == len(s):
                return [""]
            if i in cache:
                return cache[i]
            res = []
            for j in range(i + 1, len(s) + 1):
                if s[i:j] not in words:
                    continue
                prev = dfs(j)
                w = s[i:j]
                for subs in prev:
                    res.append(w if len(subs) == 0 else  w + " " + subs)
            cache[i] = res
            return res
        
        words = set(wordDict)
        cache = dict()
        return dfs(0)