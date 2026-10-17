class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pos = [0 for _ in range(26)]
        for i, ch in enumerate(order):
            pos[ord(ch) - ord('a')] = i
        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            n1, n2 = len(w1), len(w2)
            for j in range(min(n1, n2)):
                if w1[j] != w2[j]:
                    if pos[ord(w1[j]) - ord('a')] > pos[ord(w2[j]) - ord('a')]:
                        return False
                    break
                else:
                    if j == n2 - 1 and n1 > n2:
                        return False
        return True