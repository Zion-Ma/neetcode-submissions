class Node:
    def __init__(self):
        self.wordend = False
        self.children = dict()

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = Node()
            curr = curr.children[w]
        curr.wordend = True

    def search(self, word: str) -> bool:
        def dfs(i: int, curr: Node) -> bool:
            if i == len(word):
                return curr.wordend
            if word[i] == '.':
                for ch in curr.children.keys():
                    if dfs(i + 1, curr.children[ch]):
                        return True
                return False
            else:
                if word[i] not in curr.children.keys():
                    return False
                return dfs(i + 1, curr.children[word[i]])
        return dfs(0, self.root)
