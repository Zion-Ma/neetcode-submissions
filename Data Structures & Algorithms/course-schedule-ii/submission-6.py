class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            preq[c].append(p)
        ans = []
        visited = [0 for _ in range(numCourses)]
        def dfs(i):
            if visited[i] == 2:
                return True
            if visited[i] == 1:
                return False
            visited[i] = 1
            for nei in preq[i]:
                if not dfs(nei):
                    return False
            ans.append(i)
            visited[i] = 2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans        