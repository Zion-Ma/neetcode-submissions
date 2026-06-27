class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        prev2, prev1 = 0, cost[0]
        for i in range(1, len(cost)):
            curr = min(prev2, prev1) + cost[i]
            prev2, prev1 = prev1, curr
        return min(prev1, prev2)
