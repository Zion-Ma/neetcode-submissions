class Solution:
    def mySqrt(self, x: int) -> int:
        low, up = 0, x
        res = 0
        while low <= up:
            m = low + (up - low) // 2
            sq = m * m
            if sq > x:
                up = m - 1
            elif sq < x:
                low = m + 1
                res = m
            else:
                return m
        return res