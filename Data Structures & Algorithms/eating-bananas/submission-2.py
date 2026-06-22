class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def trialTime(k: int) -> int:
            t = 0
            for p in piles:
                t += math.ceil(p / k)
            return t
        start, end = 1, max(piles)
        while start <= end:
            mid = start + (end - start) // 2
            time = trialTime(mid)
            if time > h:
                start = mid + 1
            else:
                 end = mid - 1
        return start