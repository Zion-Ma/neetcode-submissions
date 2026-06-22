class Solution:
    def hammingWeight(self, n: int) -> int:
        x = str(bin(n))
        count = 0
        for i in range(len(x)):
            if x[i] == "1":
                count += 1
        return count