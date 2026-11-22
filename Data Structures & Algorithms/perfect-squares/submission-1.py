class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        factor = 1
        while factor * factor <= n:
            squares.append(factor * factor)
            factor += 1
        dp = [float("inf") for _ in range(n + 1)]
        dp[0] = 0
        for i in range(n + 1):
            for s in squares:
                diff = i - s
                if diff < 0:
                    break
                dp[i] = min(1 + dp[diff], dp[i])
        return dp[n]