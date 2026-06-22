class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count = [0] * 26
        s2Count = [0] * 26
        for i in range(len(s1)):
            pos1 = ord(s1[i]) - ord("a")
            pos2 = ord(s2[i]) - ord("a")
            s1Count[pos1] += 1
            s2Count[pos2] += 1
        if s1Count == s2Count:
            return True
        for i in range(len(s1), len(s2)):
            s2Count[ord(s2[i - len(s1)]) - ord("a")] -= 1
            s2Count[ord(s2[i]) - ord("a")] += 1
            if s1Count == s2Count:
                return True
        return False