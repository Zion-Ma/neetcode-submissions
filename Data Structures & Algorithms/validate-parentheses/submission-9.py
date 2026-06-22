class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        pair = {"}":"{", "]":"[", ")":"("}
        stack = []
        for item in s:
            if item not in pair:
                stack.append(item)
            else:
                if len(stack) == 0 or pair[item] != stack[-1]:
                    return False
                stack.pop(-1)
        return len(stack) == 0