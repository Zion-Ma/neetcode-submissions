class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        start = 0
        charDict = defaultdict(int)
        maxKey = ""
        for i, ch in enumerate(s):
            charDict[ch] += 1
            if charDict[ch] > charDict[maxKey]:
                maxKey = ch
            if (i - start + 1) - charDict[maxKey] > k:
                charDict[s[start]] -= 1
                start += 1
            maxLen = max(maxLen, i - start + 1)
        return maxLen

