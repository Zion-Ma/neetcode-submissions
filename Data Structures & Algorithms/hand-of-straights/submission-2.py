class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        counter = Counter(hand)
        sorted_key = sorted(counter.keys())
        for key in sorted_key:
            for _ in range(counter[key]):
                for i in range(key, key + groupSize):
                    if i not in counter or counter[i] == 0:
                        return False
                    counter[i] -= 1
        return True


