class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for preq, course in prerequisites:
            adj[preq].append(course)
        reachable = [[False for _ in range(numCourses)] for _ in range(numCourses)]
        for root in range(numCourses):
            queue = deque([root])
            while queue:
                node = queue.popleft()
                for nei in adj[node]:
                    if not reachable[root][nei]:
                        reachable[root][nei] = True
                        # reachable[node][nei] = True
                        queue.append(nei)
        res = []
        for u, v in queries:
            res.append(reachable[u][v])
        return res

            
