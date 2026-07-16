class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        def dfs(i: int) -> int:
            if i in dp:
                return dp[i]
            res = 1 + dfs(i + 1) # skip this one
            curr = trie.root # trie structure for word
            for j in range(i, len(s)):
                if s[j] not in curr.child:
                    break
                curr = curr.child[s[j]]
                if curr.word_end:
                    res = min(res, dfs(j + 1))
            dp[i] = res
            return res
        dp = {len(s):0}
        trie = Trie()
        for word in dictionary:
            trie.add(word)
        return dfs(0)

class Node:
    def __init__(self) -> None:
        self.child = dict()
        self.word_end = False

class Trie:
    def __init__(self) -> None:
        self.root = Node()
    
    def add(self, word) -> None:
        curr = self.root
        for w in word:
            if w not in curr.child:
                curr.child[w] = Node()
            curr = curr.child[w]
        curr.word_end = True
