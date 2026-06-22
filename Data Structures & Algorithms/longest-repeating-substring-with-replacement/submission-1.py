class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, ans = 0, 0
        freq = defaultdict(int)
        maxfreq = 0
        for j, c in enumerate(s):
            freq[c] += 1
            curr = j - i + 1
            maxfreq = max(maxfreq, freq[c])
            if (curr - maxfreq) > k:
                freq[s[i]] -= 1
                i += 1 
                curr = j - i + 1
            ans = max(ans,curr)
        return ans