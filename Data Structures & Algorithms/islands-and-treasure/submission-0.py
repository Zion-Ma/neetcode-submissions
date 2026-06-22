"""
1. 
"""

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = []
        m, n = len(grid), len(grid[0])
        visit = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visit.add((i, j))
        def add(i, j):
            if not 0 <= i < m or not 0 <= j < n or (i, j) in visit or grid[i][j] == -1:
                return
            visit.add((i, j))
            queue.append((i, j))
        dist = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                grid[i][j] = dist
                add(i + 1, j)
                add(i - 1, j)
                add(i, j + 1)
                add(i, j - 1)
            dist += 1


        