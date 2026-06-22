class Node:
    def __init__(self):
        self.children = dict()
        self.word_end = False

class PrefixTree:

    def __init__(self):
        self.word_dict = Node()

    def insert(self, word: str) -> None:
        curr = self.word_dict
        for w in word:
            if w not in curr.children:
                curr.children[w] = Node()
            curr = curr.children[w]
        curr.word_end = True

    def search(self, word: str) -> bool:
        curr = self.word_dict
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return curr.word_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.word_dict
        for w in prefix:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return True
        
        