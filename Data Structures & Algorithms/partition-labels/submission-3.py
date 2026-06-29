class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = defaultdict(int)
        for i, ch in enumerate(s):
            pos[ch] = i
        curr_max_reach = 0
        size = 0
        ans = []
        for i, ch in enumerate(s):
            size += 1
            curr_max_reach = max(curr_max_reach, pos[ch])
            if i == curr_max_reach:
                ans.append(size)
                size = 0
        return ans

