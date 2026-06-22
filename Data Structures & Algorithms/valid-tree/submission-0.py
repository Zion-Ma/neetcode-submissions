class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        visited = set()
        def DFS(v: int, prev: int) -> True:
            visited.add(v)
            for n in graph[v]:
                if n == prev:
                    continue
                if n in visited:
                    return False
                DFS(n, v)
            return True
        return DFS(0, -1) and len(visited) == n
            