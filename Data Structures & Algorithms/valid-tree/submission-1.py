class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        visited = set()
        def DFS(v: int, prev: int) -> True:
            if v in visited:
                return False
            visited.add(v)
            for n in graph[v]:
                if n == prev:
                    continue
                if not DFS(n, v):
                    return False
            return True
        return DFS(0, -1) and len(visited) == n
            