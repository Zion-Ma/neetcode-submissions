class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(o: int, c: int, curr) -> None:
            if (o == n and c == n):
                result.append(''.join(curr.copy()))
                return
            if c > o or (o + c == 2 * n and o > c):
                return
            curr.append("(")
            dfs(o + 1, c, curr)
            curr.pop()
            curr.append(")")
            dfs(o, c + 1, curr)
            curr.pop()
            
        result = []
        dfs(0, 0, [])
        return result