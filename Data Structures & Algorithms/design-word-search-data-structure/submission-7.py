class Node:
    def __init__(self) -> None:
        self.word_map = dict()
        self.word_end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.word_map:
                curr.word_map[w] = Node()
            curr = curr.word_map[w]
        curr.word_end = True

    def search(self, word: str) -> bool:
        def dfs(curr_node: Node, idx: int) -> bool:
            if idx == len(word):
                return curr_node.word_end
            if word[idx] == ".":
                for w in curr_node.word_map.keys():
                    if dfs(curr_node.word_map[w], idx + 1):
                        return True
                return False
            else:
                if word[idx] not in curr_node.word_map.keys():
                    return False
                return dfs(curr_node.word_map[word[idx]], idx + 1)
        return dfs(self.root, 0)
