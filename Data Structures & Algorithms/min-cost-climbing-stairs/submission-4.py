class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        next1, next2 = cost[-2], cost[-1]
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = cost[i] + min(next1, next2)
            next1, next2 = cost[i], next1
        return min(cost[0], cost[1])