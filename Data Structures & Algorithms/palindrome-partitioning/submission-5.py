class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        n = len(s)
        def dfs(i: int, curr: list) -> None:
            if i == n:
                result.append(curr.copy())
                return
            for j in range(i, n):
                if self.isPali(s, i, j):
                    curr.append(s[i:j+1])
                    dfs(j + 1, curr)
                    curr.pop()
        dfs(0, [])
        return result

    def isPali(self, s: str, i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
