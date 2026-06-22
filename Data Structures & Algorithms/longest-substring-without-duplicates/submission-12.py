class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        wordDict = dict()
        maxLen = 0
        last = 0
        for i, ch in enumerate(s):
            if ch in wordDict:
                last = max(wordDict[ch] + 1, last)
            wordDict[ch] = i
            maxLen = max(maxLen, i - last + 1)
            print(wordDict)
            print(last)
            print(f"{ch}, {maxLen}")
        return maxLen
