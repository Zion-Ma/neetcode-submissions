class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pos = {ch: i for i, ch in enumerate(order)}
        for i in range(1, len(words)):
            word1, word2 = words[i - 1], words[i]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if pos[word1[j]] > pos[word2[j]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True