class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sort = sorted(counter.items(), key = lambda x:x[1], reverse = True)
        return [key for key, value in sort[:k]]