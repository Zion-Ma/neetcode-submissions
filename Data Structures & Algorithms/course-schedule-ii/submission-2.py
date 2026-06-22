"""
1. build in-degree and prereq map
2. put vertex that have no inward edges into queue
3. pop element from queue, check its neighbors indegree, put its neighbors if no more inward nodes
4. repeat until nothing left in queue
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = {i:0 for i in range(numCourses)}
        preq = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            indegree[p] += 1
            preq[c].append(p)
        queue = []
        output = []
        finish = 0
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                output.append(curr)
                finish += 1
                for n in preq[curr]:
                    indegree[n] -= 1
                    if indegree[n] == 0:
                        queue.append(n)
        if finish != numCourses:
            return []
        return output[::-1]       