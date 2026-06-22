class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(i, j, ocean, prev):
            if (
                not 0 <= i < m or 
                not 0 <= j < n or 
                (i, j) in ocean or 
                heights[i][j] < prev
            ):
                return
            ocean.add((i, j))
            dfs(i + 1, j, ocean, heights[i][j])
            dfs(i - 1, j, ocean, heights[i][j])
            dfs(i, j + 1, ocean, heights[i][j])
            dfs(i, j - 1, ocean, heights[i][j])
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()
        for i in range(m):
            dfs(i, 0, pac, 0)
            dfs(i, n - 1, atl, 0)
        for i in range(n):
            dfs(0, i, pac, 0)
            dfs(m - 1, i, atl, 0)
        joint = pac.intersection(atl)
        ans = [list(x) for x in joint]
        return ans