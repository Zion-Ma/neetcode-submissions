class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        items = freq.items()
        sortedFreq = sorted(items, key = lambda x:x[1], reverse = True)[:k]
        return [x[0] for x in sortedFreq]