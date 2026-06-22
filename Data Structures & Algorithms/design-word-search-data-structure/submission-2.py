class Node:
    def __init__(self):
        self.children = dict()
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = Node()
            curr = curr.children[w]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            curr = root
            # if i == len(word):
            #     return True
            for j in range(i, len(word)):
                w = word[j]
                if w == ".":
                    for child in curr.children.keys():
                        if dfs(j + 1, curr.children[child]):
                            return True
                    return False
                else:
                    if w not in curr.children:
                        return False
                    curr = curr.children[w]
            return curr.end
        return dfs(0, self.root)
