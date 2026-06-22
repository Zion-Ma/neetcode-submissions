class Solution:
    def isValid(self, s: str) -> bool:
        pair = {"}":"{", ")":"(", "]":"["}
        stack = []
        for ch in s:
            if ch not in pair:
                stack.append(ch)
            else:
                if stack.__len__() == 0 or stack[-1] != pair[ch]:
                    return False
                else:
                    stack.pop()
        return stack.__len__() == 0