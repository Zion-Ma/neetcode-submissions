class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1
        if endWord not in wordList:
            return 0
        wordNum = 0
        adj = defaultdict(list)
        visited = set()
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]
                adj[key].append(word)
        queue = deque([beginWord])
        while queue:
            # print(queue)
            wordNum += 1
            currLen = len(queue)
            for _ in range(currLen):
                curr = queue.popleft()
                if curr == endWord:
                    return wordNum
                for i in range(len(curr)):
                    key = curr[:i] + '*' + curr[i + 1:]
                    # print(key)
                    if key not in adj:
                        continue
                    for word in adj[key]:
                        if word in visited:
                            continue
                        queue.append(word)
                        visited.add(word)
                    del adj[key]
        return 0