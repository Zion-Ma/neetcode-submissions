from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        pair_book = {"]":"[", "}":"{", ")":"("}
        close = ")}]"
        stack = deque()
        for char in s:
            if char in close:
                if len(stack) == 0 or pair_book[char] != stack[0]:
                    return False
                else:
                    stack.popleft()
            else:
                stack.appendleft(char)
        if len(stack) == 0:
            return True
        else:
            return False
        
        