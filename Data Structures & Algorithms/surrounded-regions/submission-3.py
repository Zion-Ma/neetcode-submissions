class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = list()
        seen = set()
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == "O":
                    queue.append((i, j))
                    board[i][j] = "#"
        for i in range(n):
            for j in [0, m - 1]:
                if board[j][i] == "O":
                    queue.append((j, i))
                    board[j][i] = "#"
        while queue:
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    r, c = i + di, j + dj
                    if (
                        not m > r >= 0 or\
                        not n > c >= 0 or\
                        board[r][c] != "O"
                    ): continue
                    board[r][c] = "#"
                    queue.append((r, c))
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
        return
                
        
