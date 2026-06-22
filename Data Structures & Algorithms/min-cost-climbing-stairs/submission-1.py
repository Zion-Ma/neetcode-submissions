class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp(i) = cost[i] + min(dp(i+1), dp(i+2))
        # with dp(n) = dp(n+1) = 0
        next1, next2 = 0, 0   # dp(i+1), dp(i+2) for the "beyond the top" base

        # iterate i = n-1, n-2, ..., 0
        for c in reversed(cost):
            curr = c + min(next1, next2)
            # roll: 
            #   next2 ← old next1   (becomes dp((i-1)+2) = dp(i+1))
            #   next1 ← curr        (becomes dp((i-1)+1) = dp(i))
            next2, next1 = next1, curr

        # at the end, next1 = dp(0), next2 = dp(1)
        return min(next1, next2)


        