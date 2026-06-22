class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        deg = {i:0 for i in range(numCourses)}
        preq = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            deg[p] += 1
            preq[c].append(p)
        finish = 0
        output, queue = [], []
        for key, val in deg.items():
            if val == 0:
                queue.append(key)
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                output.append(curr)
                finish += 1
                for nei in preq[curr]:
                    deg[nei] -= 1
                    if deg[nei] == 0:
                        queue.append(nei)
        if finish != numCourses:
            return []
        return output[::-1]