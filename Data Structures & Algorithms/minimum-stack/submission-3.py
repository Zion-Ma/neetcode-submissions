class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = 0

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.mini = val
        else:
            self.stack.append(val - self.mini)
            self.mini = min(val, self.mini)

    def pop(self) -> None:
        top = self.stack.pop()
        if top < 0:
            self.mini -= top

    def top(self) -> int:
        top = self.stack[-1]
        return self.mini if top <= 0 else self.mini + top

    def getMin(self) -> int:
        return self.mini
