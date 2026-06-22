class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diag = set()
        neg_diag = set()
        res = []
        board = [["."] * n for _ in range(n)]
        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if r - c in neg_diag or r + c in pos_diag or c in cols:
                    continue
                neg_diag.add(r - c)
                pos_diag.add(r + c)
                cols.add(c)
                board[r][c] = "Q"
                backtrack(r + 1)
                neg_diag.discard(r - c)
                pos_diag.discard(r + c)
                cols.discard(c)
                board[r][c] = "."
        backtrack(0)
        return res
