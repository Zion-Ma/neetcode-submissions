class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        m, n = len(word1), len(word2)
        ans = []
        while i < m or j < n:
            w1 = word1[i] if i < m else ""
            w2 = word2[j] if j < n else ""
            ans.append(w1 + w2)
            i += 1
            j += 1
        return "".join(ans)