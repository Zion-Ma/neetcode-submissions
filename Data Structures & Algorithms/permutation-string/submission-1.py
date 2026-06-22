class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = s1.__len__(), s2.__len__()
        if n1 > n2:
            return False
        freq1, freq2 = defaultdict(int), defaultdict(int)
        for i in range(n1):
            freq1[s1[i]] += 1
            freq2[s2[i]] += 1
        matches = 0
        for i in range(26):
            ch = chr(ord("a") + i)
            matches += (1 if freq1[ch] == freq2[ch] else 0)
        start = 0
        for end in range(n1, n2):
            if matches == 26:
                return True
            key = s2[end]
            freq2[key] += 1
            if freq2[key] == freq1[key]:
                matches += 1
            elif freq2[key] == freq1[key] + 1:
                matches -= 1
            key = s2[start]
            freq2[key] -= 1
            if freq2[key] == freq1[key]:
                matches += 1
            elif freq2[key] == freq1[key] - 1:
                matches -= 1
            start += 1
        return matches == 26