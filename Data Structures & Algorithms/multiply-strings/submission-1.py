class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        product = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                n1 = ord(num1[i]) - ord("0")
                n2 = ord(num2[j]) - ord("0")
                p = n1 * n2 + product[i + j + 1]
                product[i + j + 1] = p % 10
                product[i + j] += p // 10
        idx = 0
        while product[idx] == 0:
            idx += 1
        ans = ""
        for i in range(idx, len(product)):
            ans += str(product[i])
        return ans