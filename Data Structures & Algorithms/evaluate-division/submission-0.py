class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i, (a, b) in enumerate(equations):
            graph[a][b] = values[i]
            graph[b][a] = 1 / values[i]
        def dfs(src: int, target: int, visited: set) -> float:
            if src not in graph or target not in graph:
                return -1
            if src == target:
                return 1
            visited.add(src)
            for nei in graph[src]:
                if nei not in visited:
                    result = dfs(nei, target, visited)
                    if result != -1:
                        return graph[src][nei] * result
            return -1
        return [dfs(q[0], q[1], set()) for q in queries]
                



        