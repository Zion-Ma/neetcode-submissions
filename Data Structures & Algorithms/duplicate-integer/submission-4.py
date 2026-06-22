class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                return True
        return False

         