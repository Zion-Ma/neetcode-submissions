class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: list[int] = []
        for t in tokens:
            if t == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 + n2)
            elif t == "*":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 * n2)
            elif t == "-":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1)
            elif t == "/":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(float(n2)/n1))
            else:
                stack.append(int(t))
            print(stack)
        return stack[0]