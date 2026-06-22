class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        res = 0
        word_len = wordList[0].__len__()
        graph = defaultdict(list)
        for word in wordList:
            for i in range(word_len):
                pattern = word[:i] + "*" + word[i + 1:]
                graph[pattern].append(word)
        queue = [beginWord]
        visit = set()
        visit.add(beginWord)
        while queue:
            res += 1
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr == endWord:
                    return res
                for i in range(word_len):
                    pattern = curr[:i] + "*" + curr[i + 1:]
                    for neigh in graph[pattern]:
                        if neigh not in visit:
                            visit.add(neigh)
                            queue.append(neigh)
        return 0
