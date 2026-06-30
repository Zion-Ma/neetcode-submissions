class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n *= (-1)
        if n == 1:
            return x
        half = self.myPow(x, n // 2)
        res = half * half * x if n % 2 else half * half
        return res
        