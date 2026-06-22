class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, e = 0, numbers.__len__() - 1
        while s < e:
            left, right = numbers[s], numbers[e]
            if left + right == target:
                return [s + 1, e + 1]
            elif left + right > target:
                e -= 1
            else:
                s += 1
        return []
                

        