class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, ans = 0, 0
        freq = defaultdict(int)
        m = 0
        for j, c in enumerate(s):
            freq[c] += 1
            curr = j - i + 1
            m = max(m, freq[c])
            if (curr - m) > k:
                freq[s[i]] -= 1
                i += 1
                curr = j - i + 1
            ans = max(curr, ans)
        return ans
        