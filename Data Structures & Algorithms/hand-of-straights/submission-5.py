class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        record = Counter(hand)
        hand.sort()
        for num in hand:
            if record[num] == 0:
                continue
            for curr_num in range(num + 1, num + groupSize):
                if record.get(curr_num, 0) == 0:
                    return False
                record[curr_num] -= 1
            record[num] -= 1
        return sum([value for _ , value in record.items()]) == 0