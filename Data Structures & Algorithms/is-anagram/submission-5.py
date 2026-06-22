from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t) or len(s) == 0 or len(t) == 0:
        #     return False
        sc = Counter(s)
        tc = Counter(t)
        return sc == tc
            
        

        