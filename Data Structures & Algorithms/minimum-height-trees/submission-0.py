class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        degree = [0 for _ in range(n)]
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            degree[u] += 1
            graph[v].append(u)
            degree[v] += 1
        queue = deque()
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)
        while n > 2:        
            size = len(queue)
            n -= size
            for _ in range(size):
                curr = queue.popleft()
                for nei in graph[curr]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        queue.append(nei)
        return list(queue)
        
        