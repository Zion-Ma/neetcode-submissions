class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        time = [[p, float("inf") if s == 0 else (target - p) / s] for p, s in zip(position, speed)]
        time = sorted(time, key = lambda x:x[0])
        for i in range(len(time) - 1, -1, -1):
            if not stack or time[i][1] > stack[-1]:
                stack.append(time[i][1])
        return len(stack)