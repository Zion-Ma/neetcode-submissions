class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            new = 0
            while n:
                new += pow(n % 10, 2)
                n //= 10
            n = new
        return True
