class Solution:
    def isValid(self, s: str) -> bool:
        charMap = {"]":"[", "}":"{", ")":"("}
        stack = []
        for char in s:
            if char not in charMap:
                stack.append(char)
            else:
                if not stack or stack[-1] != charMap[char]:
                    return False
                stack.pop()
        return len(stack) == 0