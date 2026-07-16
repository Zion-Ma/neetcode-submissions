class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for curr in asteroids:
            if curr > 0:
                stack.append(curr)
            else:
                while stack and stack[-1] > 0 and curr != 0:
                    temp = stack[-1]
                    if abs(curr) >= abs(stack[-1]):
                        stack.pop()
                    if abs(curr) <= abs(temp):
                        curr = 0
                if curr != 0:
                    stack.append(curr)
        return stack