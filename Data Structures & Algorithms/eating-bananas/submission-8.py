class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        least, most = 1, max(piles)
        k = most
        while least < most:
            rate = least + (most - least) // 2
            hours = 0
            for p in piles:
                hours += (p + rate - 1) // rate
            if hours > h: # meaning rate too small
                 least = rate + 1
            else:
                k = min(k, rate)
                most = rate
        return k
