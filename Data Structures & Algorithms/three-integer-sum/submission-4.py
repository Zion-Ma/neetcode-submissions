from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pos, neg, z = [], [], 0
        triple = set()
        for n in nums:
            if n > 0:
                pos.append(n)
            elif n < 0:
                neg.append(n)
            else:
                z += 1
        pos_set, neg_set = set(pos), set(neg)
        # if 0 exists
        if z:
            for p in pos_set:
                if -p in neg_set:
                    triple.add((p, 0, -p))
            if z > 2:
                triple.add((0, 0, 0))
        for x, y in combinations(pos, 2):
            if -(x + y) in neg_set:
                triple.add(tuple(sorted([x, y, -(x + y)])))
        for x, y in combinations(neg, 2):
            if -(x + y) in pos_set:
                triple.add(tuple(sorted([x, y, -(x + y)])))
        return [list(tri) for tri in triple]

        
        
        