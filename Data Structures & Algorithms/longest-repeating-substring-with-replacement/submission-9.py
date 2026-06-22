class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        start = 0
        charDict = defaultdict(int)
        maxCharLen = 0
        for i, ch in enumerate(s):
            charDict[ch] += 1
            maxCharLen = max(charDict.values())
            if (i - start + 1) - maxCharLen > k:
                charDict[s[start]] -= 1
                start += 1
            maxLen = max(maxLen, i - start + 1)
        return maxLen

