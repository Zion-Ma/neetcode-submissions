class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            graph[c].append(p)
        status = [0] * numCourses
        output = []
        def dfs(i):
            if status[i] == 2:
                return True
            if status[i] == 1:
                return False
            status[i] = 1
            for n in graph[i]:
                if not dfs(n):
                    return False
            status[i] = 2
            output.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output
        