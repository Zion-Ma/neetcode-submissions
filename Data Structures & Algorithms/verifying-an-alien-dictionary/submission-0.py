class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pos = dict()
        for i, ch in enumerate(order):
            pos[ch] = i
        for i in range(1, len(words)):
            word1, word2 = words[i - 1], words[i]
            n1, n2 = len(word1), len(word2)
            shorter = min(n1, n2)
            for j in range(shorter):
                if j == n2 - 1 and word1[j] == word2[j]:
                    return False
                if word1[j] != word2[j]:
                    if  pos[word1[j]] > pos[word2[j]]:
                        return False
                    break
        return True