class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for curr in asteroids:
            if curr > 0:
                stack.append(curr)
            else:
                while stack and stack[-1] > 0 and curr != 0:
                    diff = stack[-1] + curr
                    if diff > 0:
                        curr = 0
                    elif diff < 0:
                        stack.pop()
                    else:
                        curr = 0
                        stack.pop()
                if curr != 0:
                    stack.append(curr)
        return stack