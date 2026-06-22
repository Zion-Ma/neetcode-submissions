class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1Count = [0 for _ in range(26)]
        s2Count = [0 for _ in range(26)]
        for i in range(len(s1)):
            pos1 = ord(s1[i]) - ord("a")
            pos2 = ord(s2[i]) - ord("a")
            s1Count[pos1] += 1
            s2Count[pos2] += 1
        match = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                match += 1
        start, end = 0, len(s1)
        while end < len(s2) and match != 26:
            # dealing with end
            endPos = ord(s2[end]) - ord("a")
            if s2Count[endPos] == s1Count[endPos]:
                match -= 1
            elif s2Count[endPos] + 1 == s1Count[endPos]:
                match += 1
            s2Count[endPos] += 1
            end += 1
            # dealing with start
            startPos = ord(s2[start]) - ord("a")
            if s2Count[startPos] == s1Count[startPos]:
                match -= 1
            elif s2Count[startPos] - 1 == s1Count[startPos]:
                match += 1
            s2Count[startPos] -= 1
            start += 1
        return match == 26
            