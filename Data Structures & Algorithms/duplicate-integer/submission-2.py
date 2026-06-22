from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = defaultdict(int)
        for item in nums:
            if num_dict[item] != 0:
                return True
            num_dict[item] += 1
        return False

         