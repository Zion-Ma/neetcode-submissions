class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l, r = 1, res - 1
        while l <= r:
            k = l + (r - l) // 2
            hour = 0
            for p in piles:
                # ceiling number
                hour += -(-p // k)
            if hour <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res



        