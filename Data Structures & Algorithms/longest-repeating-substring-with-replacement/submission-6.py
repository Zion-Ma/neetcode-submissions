class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, freq, ans, max_freq = 0, dict(), 0, 0
        for i, ch in enumerate(s):
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
            max_freq = max(max_freq, freq[ch])
            curr = i - start + 1
            if curr - max_freq > k:
                freq[s[start]] -= 1
                start += 1
                curr = i - start + 1
            ans = max(curr, ans)
        return ans