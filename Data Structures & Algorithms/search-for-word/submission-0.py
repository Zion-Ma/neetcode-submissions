class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def DFS(i: int, j: int, k: int):
            if k == word_len:
                return True
            if not (0 <= i < row_len) or not (0 <= j < col_len) or board[i][j] != word[k]:
                return False
            t = board[i][j]
            board[i][j] = ""

            if (
                DFS(i + 1, j, k + 1) |\
                DFS(i - 1, j, k + 1) |\
                DFS(i, j + 1, k + 1) |\
                DFS(i, j - 1, k + 1) 
            ):
                return True
            board[i][j] = t
            return False
        row_len = board.__len__()
        col_len = board[0].__len__()
        word_len = word.__len__()
        for i in range(row_len):
            for j in range(col_len):
                if DFS(i, j, 0):
                    return True
        return False

        