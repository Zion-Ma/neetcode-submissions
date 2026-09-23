class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)
        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            shorter = min(len(w1), len(w2))
            for j in range(shorter):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break
                if j == shorter - 1 and len(w1) > len(w2):
                    return ""
        # check if cycle exists
        def dfs(key: str) -> bool:
            if status[key] == 2:
                return False
            if status[key] == 1:
                return True
            status[key] = 1
            for nei in adj.get(key, []):
                if dfs(nei):
                    return True
            status[key] = 2
            alphabets.append(key)
            return False

        status = defaultdict(int)
        alphabets = list()
        chars = {c for word in words for c in word}
        for key in chars:
            if dfs(key):
                return ""
        return ''.join(alphabets[::-1])
                