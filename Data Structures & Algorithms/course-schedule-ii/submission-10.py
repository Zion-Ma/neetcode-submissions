class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        def dfs(curr: int) -> bool:
            if status[curr] == 2:
                return True
            if status[curr] == 1:
                return False
            status[curr] = 1
            for neighbor in graph[curr]:
                if not dfs(neighbor):
                    return False
            status[curr] = 2
            result.append(curr)
            return True
            
        status = [0] * numCourses
        graph = defaultdict(list)
        result = []
        for course, pre in prerequisites:
            graph[pre].append(course)
        for i in range(numCourses):
            if not dfs(i):
                return []
        return result[::-1]