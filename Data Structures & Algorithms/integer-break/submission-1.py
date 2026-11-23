from functools import lru_cache

class Solution:
    def integerBreak(self, n: int) -> int:
        @lru_cache(None)
        def dfs(num: int) -> int:
            if num == 1:
                return 1
            res = num if num != n else 0
            for i in range(1, num):
                res = max(res, dfs(i), i * dfs(num - i))
            return res
        return dfs(n)
            