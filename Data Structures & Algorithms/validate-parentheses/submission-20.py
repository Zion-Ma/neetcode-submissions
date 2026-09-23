class Solution:
    def isValid(self, s: str) -> bool:
        charMap = {"]":"[", "}":"{", ")":"("}
        stack = []
        for ch in s:
            if ch not in charMap:
                stack.append(ch)
            else:
                if not stack or stack[-1]!= charMap[ch]:
                    return False
                stack.pop()
        return len(stack) == 0
