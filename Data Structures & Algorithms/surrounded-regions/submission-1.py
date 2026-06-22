"""
1. mark Os at boarders and their neighbors as new charac
2. traverse the grid, mark all rest Os as X and new charac as O
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i, j):
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != "O":
                return
            board[i][j] = "."
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        m, n = len(board), len(board[0])
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == ".":
                    board[i][j] = "O"
        