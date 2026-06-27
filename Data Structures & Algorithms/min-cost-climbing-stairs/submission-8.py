class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2, prev1 = cost[0], cost[1]
        for i in range(2, len(cost)):
            curr = min(prev2, prev1) + cost[i]
            prev2, prev1 = prev1, curr
        return min(prev1, prev2)
