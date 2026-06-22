class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i:[] for i in range(n)}
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        visited = set()
        def DFS(curr, prev):
            if curr in visited: 
                return False
            visited.add(curr)
            for neighbor in graph[curr]:
                if neighbor == prev:
                    continue
                if not DFS(neighbor, curr):
                    return False
            return True
        return DFS(0, -1) and len(visited) == n
        