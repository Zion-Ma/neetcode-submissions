class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        n1, n2 = 1, 2
        curr = 0
        for _ in range(3, n + 1):
            curr = n1 + n2
            n1, n2 = n2, curr
        return curr
        