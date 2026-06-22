"""
for each ch in s
counter[ch] -= 1
considering.add(ch)
curr += 1
"""

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)
        considering = set()
        curr = 0
        ans = []
        for ch in s:
            counter[ch] -= 1
            considering.add(ch)
            curr += 1
            if counter[ch] == 0:
                considering.remove(ch)
                if len(considering) == 0:
                    ans.append(curr)
                    curr = 0
        return ans
            

