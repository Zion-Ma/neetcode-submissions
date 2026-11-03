class Solution:
    def tribonacci(self, n: int) -> int:
        Tn = [0, 1, 1]
        if n <= 2:
            return Tn[n]
        for _ in range(3, n + 1):
            temp = sum(Tn)
            Tn[0] = Tn[1]
            Tn[1] = Tn[2]
            Tn[2] = temp
        return Tn[2]