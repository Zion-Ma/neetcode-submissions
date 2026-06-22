class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        stack = []
        for p, s in zip(position, speed):
            t = (target - p) / s if s != 0 else float("inf")
            time.append((p, t))
        time.sort(key = lambda x:x[0])
        for _, t in time[::-1]:
            if not stack or stack[-1] < t:
                stack.append(t)
        return len(stack)