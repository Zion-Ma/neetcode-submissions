"""
for each bill, 3 scenes to consider:
    1. no change needed: bill = 5
        change[5] += 1
    2. requires change, do have change to give
        change[5] -= (bill - 5) // 5
    3. no change to give
        return False
"""

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                five, ten = five - 1, ten + 1
            elif ten > 0:
                five, ten = five - 1, ten - 1
            else:
                five -= 3
            if five < 0:
                return False
        return True
            
        