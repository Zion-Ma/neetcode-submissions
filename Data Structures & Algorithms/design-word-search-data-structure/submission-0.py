class Node():
    def __init__(self):
        self.children = dict()
        self.wordend = False

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
        def search_helper(idx: int, node: Node) -> bool:
            if node is None:
                return False
            if idx == word_len:
                return node.wordend
            w = word[idx]
            if w == ".":
                for key in node.children.keys():
                    if search_helper(idx + 1, node.children[key]):
                        return True
                return False
            else:
                if w not in node.children:
                    return False
                else:
                    return search_helper(idx + 1, node.children[w])
        word_len = len(word)
        return search_helper(0, self.root)
        
