class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = dict()
        for i, ch in enumerate(s):
            pos[ch] = i
        curr_max_reach = 0
        start = 0
        ans = []
        for i, ch in enumerate(s):
            curr_max_reach = max(pos[ch], curr_max_reach)
            if curr_max_reach == i:
                ans.append(i - start + 1)
                start = curr_max_reach + 1
        return ans

        