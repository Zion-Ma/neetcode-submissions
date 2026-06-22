class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        key = list(counter.keys())
        heapq.heapify(key)
        while key:
            first = key[0]
            for i in range(first, first + groupSize):
                if i not in counter:
                    return False
                counter[i] -= 1
                if counter[i] == 0:
                    if i != key[0]:
                        return False
                    heapq.heappop(key)
        return True