class Node:
    def __init__(self):
        self.children = dict()
        self.end = False

    def addWord(self, word):
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = Node()
            curr = curr.children[w]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        root = Node()
        for word in words:
            root.addWord(word)
        visit, res = set(), set()

        def dfs(i, j, curr, word):
            if (
                not 0 <= i < m or \
                not 0 <= j < n or \
                board[i][j] not in curr.children or \
                (i, j) in visit
            ):
                return
            w = board[i][j]
            curr = curr.children[w]
            word += w
            visit.add((i, j))
            if curr.end:
                res.add(word)
            dfs(i + 1, j, curr, word)
            dfs(i - 1, j, curr, word)
            dfs(i, j + 1, curr, word)
            dfs(i, j - 1, curr, word)
            visit.remove((i, j))
        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")
        return list(res)