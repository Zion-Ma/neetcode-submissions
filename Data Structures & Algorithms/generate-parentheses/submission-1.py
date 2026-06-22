class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = []
        def dfs(o, c):
            if o == c == n:
                ans.append("".join(stack))
                return
            if o < n:
                stack.append("(")
                dfs(o + 1, c)
                stack.pop()
            if c < o:
                stack.append(")")
                dfs(o, c + 1)
                stack.pop()
        dfs(0, 0)
        return ans