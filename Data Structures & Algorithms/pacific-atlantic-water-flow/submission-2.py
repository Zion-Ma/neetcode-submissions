class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(i: int, j: int, prev: int, ocean: str, seen: set) -> None:
            if (
                not m > i >= 0 or\
                not n > j >= 0 or\
                (i, j) in seen or\
                heights[i][j] < prev
            ): return
            if ocean == "pac":
                pac.add((i, j))
            else:
                atl.add((i, j))
            seen.add((i, j))
            dfs(i + 1, j, heights[i][j], ocean, seen)
            dfs(i - 1, j, heights[i][j], ocean, seen)
            dfs(i, j + 1, heights[i][j], ocean, seen)
            dfs(i, j - 1, heights[i][j], ocean, seen)
            
        
        m, n = len(heights), len(heights[0])
        atl, pac = set(), set()
        for i in range(m):
            dfs(i, 0, 0, "pac", set())
            dfs(i, n - 1, 0, "atl", set())
        
        for j in range(n):
            dfs(0, j, 0, "pac", set())
            dfs(m - 1, j, 0, "atl", set())

        ans = pac.intersection(atl)
        return [[x, y] for x, y in ans]
