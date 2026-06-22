class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1, prev2 = cost[1], cost[0]
        for i in range(2, len(cost)):
            cost[i] = cost[i] + min(prev1, prev2)
            prev1, prev2 = cost[i], prev1
        return min(prev1, prev2)