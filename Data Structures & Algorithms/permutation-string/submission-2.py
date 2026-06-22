class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = s1.__len__(), s2.__len__()
        if n1 > n2:
            return False
        freq1, freq2 = [0] * 26, [0] * 26
        for i in range(n1):
            idx1, idx2 = ord(s1[i]) - ord("a"), ord(s2[i]) - ord("a")
            freq1[idx1] += 1
            freq2[idx2] += 1
        matches = 0
        for i in range(26):
            if freq1[i] == freq2[i]:
                matches += 1
        start = 0
        for i in range(n1, n2):
            if matches == 26:
                return True
            idx = ord(s2[i]) - ord("a")
            freq2[idx] += 1
            if freq2[idx] == freq1[idx]:
                matches += 1
            elif freq2[idx] == freq1[idx] + 1:
                matches -= 1
            idx = ord(s2[start]) - ord("a")
            freq2[idx] -= 1
            if freq2[idx] == freq1[idx]:
                matches += 1
            elif freq2[idx] == freq1[idx] - 1:
                matches -= 1
            start += 1
        return matches == 26
