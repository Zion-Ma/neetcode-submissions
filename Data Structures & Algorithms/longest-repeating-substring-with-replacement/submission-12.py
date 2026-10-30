class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0 for _ in range(26)]
        left = 0
        ans = 0
        for i, ch in enumerate(s):
            # print(ord(ch) - ord('A'))
            freq[ord(ch) - ord('A')] += 1
            max_freq = max(freq)
            while i - left + 1 - max_freq > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
                max_freq = max(freq)
            ans = max(ans, i - left + 1)
        return ans
