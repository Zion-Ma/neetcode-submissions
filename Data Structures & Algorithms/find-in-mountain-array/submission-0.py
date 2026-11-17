class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # find the peak
        lo, hi = 0, mountainArr.length() - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid + 1 < mountainArr.length() - 1 and mountainArr.get(mid) < mountainArr.get(mid + 1):
                lo = mid + 1
            else:
                hi = mid
        peak = hi
        # search from [0:peak]
        lo, hi = 0, peak - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mountainArr.get(mid) == target:
                return mid
            if mountainArr.get(mid) > target:
                hi = mid - 1
            else:
                lo = mid + 1
        # search from [peak:]
        lo, hi = peak, mountainArr.length() - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mountainArr.get(mid) == target:
                return mid
            if mountainArr.get(mid) > target:
                lo = mid + 1
            else:
                hi = mid - 1
        # return -1 if no match
        return -1