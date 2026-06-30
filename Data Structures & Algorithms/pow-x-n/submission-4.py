class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1:
            return x
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n *= (-1)
        half = self.myPow(x, n // 2)
        res = half * half * x if n % 2 else half * half
        return res
        