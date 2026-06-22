class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sort = sorted([(p, s) for p, s in zip(position, speed)])[::-1]
        stack = []
        for p, s in sort:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)