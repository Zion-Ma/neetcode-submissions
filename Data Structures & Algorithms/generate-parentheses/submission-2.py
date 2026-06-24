class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def generate(curr_str: str, o: int, c: int) -> None:
            if o == n and c == n:
                ans.append(curr_str[:])
                return
            if len(curr_str) == 2 * n and (o > n or c > n):
                return
            if c > o:
                return
            curr_str += "("
            generate(curr_str, o + 1, c)
            curr_str = curr_str[:-1]
            curr_str += ")"
            generate(curr_str, o, c + 1)
            curr_str = curr_str[:-1]
            return
        generate("(", 1, 0)
        return ans
