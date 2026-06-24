class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        if n == 0:
            return []
        ans = []
        def dfs(i: int, part: list) -> None:
            if i == n:
                ans.append(part.copy())
                return
            for j in range(i, n):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1, part)
                    part.pop()
            return
        dfs(0, [])
        return ans

    def isPali(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1
        return True