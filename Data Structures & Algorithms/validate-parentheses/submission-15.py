class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {"]":"[", "}":"{", ")":"("}
        for ch in s:
            if ch not in pair:
                stack.append(ch)
            else:
                if len(stack) == 0 or stack.pop() != pair[ch]:
                    return False
        return len(stack) == 0