class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        deg = {i:0 for i in range(numCourses)}
        graph = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            deg[p] += 1
            graph[c].append(p)
        output, queue = [], []
        finish = 0
        for key, val in deg.items():
            if val == 0:
                queue.append(key)
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                output.append(curr)
                finish += 1
                for n in graph[curr]:
                    deg[n] -= 1
                    if deg[n] == 0:
                        queue.append(n)
        if finish != numCourses:
            return []
        return output[::-1]

