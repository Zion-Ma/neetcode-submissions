class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i
        start, end = 0, 0
        ans = []
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if end == i:
                ans.append(end - start + 1)
                start = end + 1
        return ans
