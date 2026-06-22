class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        maxKey = ""
        maxLen = 0
        start = 0
        for i, ch in enumerate(s):
            freq[ch] += 1
            if freq[maxKey] < freq[ch]:
                maxKey = ch
            if (i - start + 1) - freq[maxKey] > k:
                freq[s[start]] -= 1
                start += 1
            maxLen = max(maxLen, i - start + 1)
        return maxLen