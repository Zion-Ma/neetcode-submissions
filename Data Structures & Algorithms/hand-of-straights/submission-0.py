"""
while key is non-empty
pop top
if counter[top] == 0; continue
do x to x + GS - 1; 
if counter[i] == 0 return False; otherwise counter[i] - 1
if counter[top] > 0: push top back to key
repeat until 
"""

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        counter = Counter(hand)
        key = list(counter.keys())
        heapq.heapify(key)
        while key:
            least = heapq.heappop(key)
            if counter[least] == 0:
                continue
            for i in range(least, least + groupSize):
                if i not in counter or counter[i] == 0:
                    return False
                counter[i] -= 1
            if counter[least] > 0:
                heapq.heappush(key, least)
        return True

