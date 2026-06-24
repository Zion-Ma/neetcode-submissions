class Node:
    def __init__(self) -> None:
        self.word_map = dict()
        self.word_stop = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.word_map:
                curr.word_map[w] = Node()
            curr = curr.word_map[w]
        curr.word_stop = True

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w not in curr.word_map:
                return False
            curr = curr.word_map[w]
        return curr.word_stop

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            if w not in curr.word_map:
                return False
            curr = curr.word_map[w]
        return True
        
        