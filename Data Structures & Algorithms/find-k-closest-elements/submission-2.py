class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while (r - l + 1) > k:
            left_dist = abs(x - arr[l])
            right_dist = abs(x - arr[r])
            if left_dist > right_dist:
                l += 1
            else:
                r -= 1
        return arr[l:r + 1]