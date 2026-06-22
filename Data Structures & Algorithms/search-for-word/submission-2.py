class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        word_len = len(word)
        def backtrack(i, j, k) -> bool:
            if k == word_len:
                return True
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k]:
                return False
            temp = board[i][j]
            board[i][j] = ""
            if (
                backtrack(i + 1, j, k + 1) or \
                backtrack(i - 1, j, k + 1) or \
                backtrack(i, j + 1, k + 1) or \
                backtrack(i, j - 1, k + 1)
            ):
                return True
            board[i][j] = temp
            return False
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False