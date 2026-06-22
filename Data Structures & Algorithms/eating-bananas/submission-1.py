class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        n = piles.__len__()
        l, r = 1, res - 1
        while l <= r:
            mid = l + (r - l) // 2
            hours = 0
            for i in range(n):
                hours += math.ceil(piles[i] / mid)
            if hours > h:
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid - 1
        return res