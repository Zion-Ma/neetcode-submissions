class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1
        queue = [i for i in range(numCourses) if in_degree[i] == 0]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return result if len(result) == numCourses else []