class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        visited = [0] * n
        graph = {i:[] for i in range(n)}
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        def dfs(i, prev):
            if visited[i] == 2:
                return True
            if visited[i] == 1:
                return False
            visited[i] = 1
            for nei in graph[i]:
                if nei == prev:
                    continue
                if not dfs(nei, i):
                    return False
            visited[i] = 2
            return True
        for i in range(n):
            if not dfs(i, -1):
                return False
        return len(visited) == n