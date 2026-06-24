class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        ans = []
        digit_map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def dfs(i: int, curr_str: str) -> None:
            if i == n:
                ans.append(curr_str)
                return
            for ch in digit_map[digits[i]]:
                curr_str += ch
                dfs(i + 1, curr_str)
                curr_str = curr_str[:-1]
            return
        dfs(0, "")
        return ans

        




