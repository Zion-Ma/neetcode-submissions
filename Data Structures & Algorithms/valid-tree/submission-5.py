class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = {i:[] for i in range(n)}
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        visited, cycle = set(), set()
        def dfs(i, prev):
            if i in visited:
                return True
            if i in cycle:
                return False
            cycle.add(i)
            for n in graph[i]:
                if n == prev:
                    continue
                if not dfs(n, i):
                    return False
            cycle.remove(i)
            visited.add(i)
            return True
        for i in range(n):
            if not dfs(i, -1):
                return False
        return len(visited) == n
            