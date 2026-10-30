class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0 for _ in range(26)]
        left = 0
        ans = 0
        max_freq = 0
        for i, ch in enumerate(s):
            curr = ord(ch) - ord('A')
            freq[curr] += 1
            if freq[curr] > freq[max_freq]:
                max_freq = curr
            if i - left + 1 - freq[max_freq] > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans
