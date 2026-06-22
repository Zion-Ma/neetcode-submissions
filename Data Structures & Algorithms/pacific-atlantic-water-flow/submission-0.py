class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n, pac, atl = len(heights), len(heights[0]), set(), set()
        def DFS(i, j, prev, ocean):
            if not (0 <= i < m) or not (0 <= j < n):
                return
            elif (i, j) in ocean:
                return
            elif heights[i][j] < prev:
                return
            else:
                ocean.add((i, j))
                DFS(i + 1, j, heights[i][j], ocean)
                DFS(i - 1, j, heights[i][j], ocean)
                DFS(i, j + 1, heights[i][j], ocean)
                DFS(i, j - 1, heights[i][j], ocean)
        for i in range(m):
            DFS(i, 0, -1, pac)
            DFS(i, n - 1, -1, atl)
        for i in range(n):
            DFS(0, i, -1, pac)
            DFS(m - 1, i, -1, atl)

        return list(pac & atl)

        