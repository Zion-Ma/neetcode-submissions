class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        res = 0
        outer_p = 0
        for n1 in num1[::-1]:
            p = 0
            for n2 in num2[::-1]:
                d1 = ord(n1) - ord("0")
                d2 = ord(n2) - ord("0")
                res += (d1 * pow(10, outer_p)) * (d2 * pow(10, p))
                p += 1
            outer_p += 1
        return str(res)
