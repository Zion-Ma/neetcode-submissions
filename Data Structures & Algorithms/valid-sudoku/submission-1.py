class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        blocks = [0] * 9
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                byte = 1 << eval(board[r][c])
                if (
                    rows[r] & byte or \
                    cols[c] & byte or \
                    blocks[r // 3 * 3 + c // 3] & byte
                ):
                    return False
                rows[r] |= byte
                cols[c] |= byte
                blocks[r // 3 * 3 + c // 3] |= byte
        return True