class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            prereq[c].append(p)
        visited, cycle = set(), set()
        output = []
        def dfs(i):
            if i in visited:
                return True
            if i in cycle:
                return False
            cycle.add(i)
            for neighbor in prereq[i]:
                if not dfs(neighbor):
                    return False
            cycle.remove(i)
            visited.add(i)
            output.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output      