class Node:
    def __init__(self):
        self.chd = dict()
        self.wordEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.chd:
                curr.chd[w] = Node()
            curr = curr.chd[w]
        curr.wordEnd = True

    def search(self, word: str) -> bool:
        def subSearch(curr: Node, sub: str) -> bool:
            if len(sub) == 0:
                return curr.wordEnd
            for i, ch in enumerate(sub):
                if ch == ".":
                    for k in curr.chd.keys():
                        if subSearch(curr.chd[k], sub[i + 1:]):
                            return True
                    return False
                else:
                    if ch not in curr.chd:
                        return False
                    curr = curr.chd[ch]
            return curr.wordEnd
        return subSearch(self.root, word)





