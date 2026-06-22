class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(i, curr):
            if i == n:
                res.append(curr)
                return
            for ch in digit_map[digits[i]]:
                curr += ch
                dfs(i + 1, curr)
                curr = curr[:-1]

        n = len(digits)
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        if n > 0:
            dfs(0, "")
        return res
