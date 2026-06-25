class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(i: int, j: int, prev: int, ocean_name: str) -> None:
            ocean = pac if ocean_name == "pac" else atl
            if (
                not m > i >= 0 or\
                not n > j >= 0 or\
                (i, j) in ocean or\
                heights[i][j] < prev
            ): return
            ocean.add((i, j))
            dfs(i + 1, j, heights[i][j], ocean_name)
            dfs(i - 1, j, heights[i][j], ocean_name)
            dfs(i, j + 1, heights[i][j], ocean_name)
            dfs(i, j - 1, heights[i][j], ocean_name)
            
        
        m, n = len(heights), len(heights[0])
        atl, pac = set(), set()
        for i in range(m):
            dfs(i, 0, 0, "pac")
            dfs(i, n - 1, 0, "atl")
        
        for j in range(n):
            dfs(0, j, 0, "pac")
            dfs(m - 1, j, 0, "atl")

        ans = pac.intersection(atl)
        return [[x, y] for x, y in ans]
