class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {ch:set() for w in words for ch in w}
        res = []
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            n1, n2 = len(w1), len(w2)
            m = min(n1, n2)
            if w1[:m] == w2[:m] and n1 > n2:
                return ""
            for j in range(m):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
        visited = {ch:0 for ch in graph.keys()}
        def dfs(curr: str) -> bool:
            if visited[curr] == 2:
                return True
            if visited[curr] == 1:
                return False
            visited[curr] = 1
            for nei in graph[curr]:
                if not dfs(nei):
                    return False
            visited[curr] = 2
            res.append(curr)
            return True
            
        for node in graph.keys():
            if not dfs(node):
                return ""
        return "".join(res[::-1])
        
