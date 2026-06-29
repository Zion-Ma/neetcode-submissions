class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = defaultdict(int)
        for i, ch in enumerate(s):
            pos[ch] = i
        start, end = 0, 0
        ans = []
        for i, ch in enumerate(s):
            end = max(end, pos[ch])
            if i == end:
                ans.append(end - start + 1)
                start = end + 1
        return ans

