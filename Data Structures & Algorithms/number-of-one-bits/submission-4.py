class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            count += ((1 << i) & n) != 0
        return count