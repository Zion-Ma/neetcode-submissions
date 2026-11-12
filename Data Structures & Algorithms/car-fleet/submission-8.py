class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        rate = [(p, (target - p) / s) for p, s in zip(position, speed)]
        rate.sort(key = lambda x:x[0])
        stack = []
        for i, [p, t] in enumerate(rate[::-1]):
            if stack and t <= stack[-1]:
                continue
            stack.append(t)
        return len(stack)

        