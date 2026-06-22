class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # adj = defaultdict(set)
        adj = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            n1, n2 = len(w1), len(w2)
            m = min(n1, n2)
            if w1[:m] == w2[:m] and n1 > n2:
                return ""
            for j in range(m):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visited = dict()
        res = []
        def dfs(curr):
            if curr in visited:
                return visited[curr]
            visited[curr] = True
            for nei in adj[curr]:
                if dfs(nei):
                    return True
            visited[curr] = False
            res.append(curr)
        for node in list(adj.keys()):
            if dfs(node):
                return ""
        res.reverse()
        return "".join(res)
