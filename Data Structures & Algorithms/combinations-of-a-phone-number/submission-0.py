class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        digitToChar = {
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
        def dfs(i, curr):
            if i == n:
                res.append(curr)
                return
            for ch in digitToChar[digits[i]]:
                curr += ch
                dfs(i + 1, curr)
                curr = curr[:-1]
        dfs(0, "")
        return res