class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1:
            return x
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n *= (-1)
        def self_pow(curr_n):
            if curr_n == 1:
                return x
            half = self_pow(curr_n // 2)
            return half * half * x if curr_n % 2 else half * half
        return self_pow(n)
        