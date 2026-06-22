class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        freqGroup = [[] for _ in range(len(nums) + 1)]
        result = []
        for n in nums:
            freq[n] += 1
        for key, v in freq.items():
            freqGroup[v].append(key)
        for i in range(len(nums), 0, -1):
            if freqGroup[i]:
                for key in freqGroup[i]:
                    result.append(key)
                    if len(result) == k:
                        return result
        return result
        
        