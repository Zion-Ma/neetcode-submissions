class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(i: int, j: int) -> None:
            if not(0 <= i < len(grid)) or not(0 <= j < len(grid[0])) or grid[i][j] != "1":
                return
            grid[i][j] = "0"
            helper(i + 1, j)
            helper(i - 1, j)
            helper(i, j + 1)
            helper(i, j - 1)

        island_num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    helper(i, j)
                    island_num += 1
        return island_num
        