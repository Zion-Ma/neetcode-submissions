class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, ans = 0, 0
        maxfreq = defaultdict(int)
        m = 0
        for j, c in enumerate(s):
            maxfreq[c] += 1
            m = max(m, maxfreq[c])
            curr = j - i + 1
            if curr - m > k:
                maxfreq[s[i]] -= 1
                i += 1
                curr = j - i + 1
            ans = max(ans, curr)
        return ans