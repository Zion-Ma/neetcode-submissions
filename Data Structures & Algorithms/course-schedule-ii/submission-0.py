class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            prereq[c].append(p)
        status = [0] * numCourses
        output = []
        def dfs(i):
            if status[i] == 2:
                return True
            if status[i] == 1:
                return False
            status[i] = 1
            for neighbor in prereq[i]:
                if not dfs(neighbor):
                    return False
            status[i] = 2
            output.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output      