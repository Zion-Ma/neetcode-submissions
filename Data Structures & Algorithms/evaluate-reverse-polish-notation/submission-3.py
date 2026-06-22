class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append(s1 + s2)
            elif t == "-":
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append(s1 - s2)
            elif t == "*":
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append(s1 * s2)
            elif t == "/":
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append(int(s1 / s2))
            else:
                stack.append(int(t))
        return stack[-1]
            