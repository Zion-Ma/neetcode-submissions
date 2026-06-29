class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            curr = minH[0]
            for i in range(curr, curr + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        
        return True


