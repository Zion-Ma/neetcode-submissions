class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        status = {ch:0 for word in words for ch in word}
        graph = defaultdict(list)
        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            length = min(len(w1), len(w2))
            for j in range(length):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    break
                if j == length - 1 and len(w1) > len(w2):
                    return ""
        res = []
        unvisited, visiting, visited = 0, 1, 2
        def dfs(ch: str) -> bool:
            if status[ch] == visited:
                return True
            if status[ch] == visiting:
                return False
            status[ch] = visiting
            for nei in graph[ch]:
                if not dfs(nei):
                    return False
            status[ch] = visited
            res.append(ch)
            return True
        for ch in status:
            if not dfs(ch):
                return ""
        return ''.join(res[::-1])
            
            