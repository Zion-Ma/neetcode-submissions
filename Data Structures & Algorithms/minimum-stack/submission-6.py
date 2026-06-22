class MinStack:
    # top = val - min

    def __init__(self):
        self.stack = []
        self.Min = float("inf")

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append(val - self.Min)
            if val < self.Min:
                self.Min = val
        else:
            self.stack.append(0)
            self.Min = val

    def pop(self) -> None:
        # recover the previous min
        diff = self.stack.pop()
        if diff < 0:
            self.Min -= diff

    def top(self) -> int:
        t = self.stack[-1]
        if t < 0:
            return self.Min
        else:
            return self.Min + t

    def getMin(self) -> int:
        return self.Min
