class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        record = 0
        for n in nums:
            curr = 1 << n
            if record & curr:
                return n
            record |= curr