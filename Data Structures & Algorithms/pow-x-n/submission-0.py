class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1:
            return x
        if n == 0:
            return 1
        if n < 0:
            x, n = 1 / x, -n
        def self_pow(curr_n):
            if curr_n == 1:
                return x
            return self_pow(curr_n // 2) * self_pow(curr_n - curr_n // 2)
        return self_pow(n)
            
        