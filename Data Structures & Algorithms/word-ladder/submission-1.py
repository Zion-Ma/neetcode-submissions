class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        path = dict()
        visited = set()
        word_num, word_len = 0, len(beginWord)
        queue = [beginWord]
        visited.add(beginWord)
        for word in wordList:
            for i in range(word_len):
                pattern = word[:i] + "*" + word[i + 1:]
                if pattern not in path:
                    path[pattern] = []
                path[pattern].append(word)
        while queue:
            word_num += 1
            for _ in range(len(queue)):
                word = queue.pop(0)
                # print(word)
                if word == endWord:
                    return word_num
                for i in range(word_len):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for node in path.get(pattern, []):
                        # print(node)
                        if node in visited:
                            continue
                        visited.add(node)
                        queue.append(node)
        return 0