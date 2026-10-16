class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        perim = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                perim += 4
                if (i > 0 and grid[i - 1][j] == 1):
                    perim -= 2
                if (j > 0 and grid[i][j - 1] == 1):
                    perim -= 2
        return perim