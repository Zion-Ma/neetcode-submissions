class Solution:
    def tribonacci(self, n: int) -> int:
        Tn = [0, 1, 1]
        if n <= 2:
            return Tn[n]
        for i in range(3, n + 1):
            Tn[i % 3] = sum(Tn)
        return Tn[n % 3]