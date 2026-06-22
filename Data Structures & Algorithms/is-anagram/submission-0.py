from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)) or (len(s) == 0) or (len(t) == 0):
            return False
        sd, td = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            sd[s[i]] += 1
            td[t[i]] += 1
        for sk, tk in zip(sd.keys(), td.keys()):
            if sk not in td.keys():
                return False
            else:
                if sd[sk] != td[tk]:
                    return False
        return True

        