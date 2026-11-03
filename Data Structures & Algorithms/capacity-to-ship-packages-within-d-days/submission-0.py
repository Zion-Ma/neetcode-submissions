class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        least = max(weights)
        most = sum(weights)
        res = most
        while least <= most:
            cap = least + (most - least) // 2
            d = 0
            i = 0
            curr_load = 0
            while i < len(weights):
                while i < len(weights) and curr_load + weights[i] <= cap:
                    curr_load += weights[i]
                    i += 1
                curr_load = 0
                d += 1
            if d > days:
                least = cap + 1
            else:
                res = min(cap, res)
                most = cap - 1
        return res