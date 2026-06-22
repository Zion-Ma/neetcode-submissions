"""
1. count all fresh and push freshes at boarders to visit
2. put boarder fresh's neighbors into visit (DFS)
3. traverse the entire grid to see how many fresh cannot be rotten; add 1 to minute for each step
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = []
        self.fresh = 0
        def rot(i, j):
            if not 0 <= i < m or not 0 <= j < n or grid[i][j] != 1:
                return
            grid[i][j] = 2
            queue.append((i, j))
            self.fresh -= 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        time = 0
        while queue and self.fresh > 0:
            time += 1
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                rot(i + 1, j)    
                rot(i - 1, j) 
                rot(i, j + 1) 
                rot(i, j - 1) 
        return time if self.fresh == 0 else -1    