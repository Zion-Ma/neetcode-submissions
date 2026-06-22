class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for operand in tokens:
            if operand == "+":
                stack.append(stack.pop() + stack.pop())
            elif operand == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif operand == "*":
                stack.append(stack.pop() * stack.pop())
            elif operand == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(operand))
        return stack[-1]