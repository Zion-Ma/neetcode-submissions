class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
        # 0 : unvisited, 1 : visiting, 2 : visited
        states = [0 for _ in range(numCourses)]
        def DFS(course: int) -> bool:
            state = states[course]
            if state == 2: return True
            if state == 1: return False
            states[course] = 1
            for n in graph[course]:
                if not DFS(n):
                    return False
            states[course] = 2
            return True
        for i in range(numCourses):
            if not DFS(i):
                return False
        return True
        