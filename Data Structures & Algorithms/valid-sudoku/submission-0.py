class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [0] * 9
        rows = [0] * 9
        blocks = [0] * 9
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                shift = ord(board[r][c]) - ord("1")
                mask = 1 << shift
                if (
                    rows[r] & mask or \
                    cols[c] & mask or \
                    blocks[(r // 3) * 3 + c // 3] & mask
                ):
                    return False
                rows[r] |= mask
                cols[c] |= mask
                blocks[(r // 3) * 3 + c // 3] |= mask
        return True
        