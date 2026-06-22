class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev1, prev2 = 2, 1
        for i in range(3, n + 1):
            curr = prev1 + prev2
            prev1, prev2 = curr, prev1
        return prev1