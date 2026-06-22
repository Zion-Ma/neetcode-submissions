class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        for c, preq in prerequisites:
            graph[c].append(preq)
        # 0: unvisited; 1: visiting; 2: visited
        status = [0 for _ in range(numCourses)]
        
        def dfs(c) -> bool:
            if status[c] == 2:
                return True
            if status[c] == 1:
                return False
            status[c] = 1
            for neigh in graph[c]:
                if not dfs(neigh):
                    return False
            status[c] = 2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
