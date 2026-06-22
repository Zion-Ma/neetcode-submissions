""""
1. collect 0's coordinates into queue
2. pop coordinates from queue and check their neighbors
3. repeat 1-2 until empty queue
"""

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def add(i, j):
            if not 0 <= i < m or not 0 <= j < n or grid[i][j] == -1 or (i, j) in visit:
                return
            visit.add((i, j))
            queue.append((i, j))
        
        m, n = len(grid), len(grid[0])
        queue, visit = [], set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visit.add((i, j))
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

        