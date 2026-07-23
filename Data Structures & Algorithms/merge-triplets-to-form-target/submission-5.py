class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first, second, third = False, False, False
        for x, y, z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            first |= (x == target[0])
            second |= (y == target[1])
            third |= (z == target[2])
            if first and second and third:
                return True
        return first and second and third

