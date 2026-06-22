class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        def self_pow(curr_n):
            if curr_n == 0:
                return 1
            res = self_pow(curr_n // 2)
            res = res * res
            return x * res if curr_n % 2 else res
        ans = self_pow(abs(n))
        return 1 / ans if n < 0 else ans