class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        rowDict = defaultdict(set)
        colDict = defaultdict(set)
        squareDict = defaultdict(set)
        for i in range(m):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if (
                    board[i][j] in rowDict[i] or \
                    board[i][j] in colDict[j] or \
                    board[i][j] in squareDict[(i // 3) * 3 + j // 3]
                ):
                    return False
                rowDict[i].add(board[i][j])
                colDict[j].add(board[i][j])
                squareDict[(i // 3) * 3 + j // 3].add(board[i][j])
        return True
                