class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        least, most = 1, max(piles)
        while least < most:
            m = least + (most - least) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / m)
            if hours <= h:
                most = m
            else:
                least = m + 1
        return least 
