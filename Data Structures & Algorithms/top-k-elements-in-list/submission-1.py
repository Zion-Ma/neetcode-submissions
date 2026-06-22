from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = defaultdict(int)
        for n in nums:
            num_dict[n] += 1
        return [item[0] for item in sorted(list(num_dict.items()), key = lambda x:x[1], reverse = True)[:k]]
        