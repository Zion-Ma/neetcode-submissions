class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        def canSplit(largest: int) -> bool:
            subarray_count = 1
            curr_sum = 0
            for n in nums:
                curr_sum += n
                if curr_sum > largest:
                    subarray_count += 1
                    if subarray_count > k:
                        return False
                    curr_sum = n
            return True
        res = r
        while l <= r:
            m = l + (r - l) // 2
            if canSplit(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res