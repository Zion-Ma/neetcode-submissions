class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def generate(curr_list: list, o: int, c: int) -> None:
            if o == n and c == n:
                ans.append("".join(curr_list))
                return
            if len(curr_list) == 2 * n and (o > n or c > n):
                return
            if c > o:
                return
            curr_list.append("(")
            generate(curr_list, o + 1, c)
            curr_list.pop()
            curr_list.append(")")
            generate(curr_list, o, c + 1)
            curr_list.pop()
            return
        generate(["("], 1, 0)
        return ans
