class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = nums1.__len__(), nums2.__len__()
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        total = m + n
        half = total // 2
        l, r = 0, m - 1
        while True:
            i = l + (r - l) // 2
            j = half - i - 2
            mleft = nums1[i] if i >= 0 else float("-inf")
            mright = nums1[i + 1] if i + 1 < m else float("inf")
            nleft = nums2[j] if j >= 0 else float("-inf")
            nright = nums2[j + 1] if j + 1 < n else float("inf")
            if mleft <= nright and nleft <= mright:
                if total % 2:
                    return min(mright, nright)
                else:
                    return (max(mleft, nleft) + min(mright, nright)) / 2
            elif mleft > nright:
                r = i - 1
            else:
                l = i + 1

