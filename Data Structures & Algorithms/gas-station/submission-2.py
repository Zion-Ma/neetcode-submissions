class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        canDo = 0
        accumulate = 0
        for i in range(len(gas)):
            curr = gas[i] - cost[i]
            accumulate += curr
            if accumulate < 0:
                accumulate = 0
                canDo = i + 1
        return canDo