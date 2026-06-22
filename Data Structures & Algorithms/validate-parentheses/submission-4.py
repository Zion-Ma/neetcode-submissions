class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        d = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        stack = []
        for c in s:
            if c not in d:
                stack.append(c)
            else:
                if len(stack) == 0 or stack[-1] != d[c]:
                    return False
                stack.pop(-1)
        return len(stack) == 0

