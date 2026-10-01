class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        VISITING, VISITED = 1, 2
        status = defaultdict(int)
        adj = defaultdict(list)
        result = []
        for course, preq in prerequisites:
            adj[course].append(preq)

        def dfs(node: int) -> bool:
            if status.get(node, 0) == VISITED:
                return False
            if status.get(node, 0) == VISITING:
                return True
            status[node] = VISITING
            for nei in adj.get(node, []):
                if dfs(nei):
                    return True
            status[node] = VISITED
            result.append(node)
            return False
        for node in range(numCourses):
            if dfs(node):
                return []
        return result