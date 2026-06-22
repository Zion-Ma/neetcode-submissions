"""
1. easier to do it backwards
2. start at the third from the back
3. get min of cost[i] + previous-1 and cost[i] + previous-2 and update the two pointers
4. repeat 3 until it comes to the very beginning
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        next1, next2 = cost[-2], cost[-1]
        for i in range(len(cost) - 3, -1, -1):
            curr = cost[i] + min(next1, next2)
            next1, next2 = curr, next1
        return min(next1, next2)