class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if k == len(word):
                return True
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k]:
                return False
            temp = board[i][j]
            board[i][j] = ""
            if (
                dfs(i + 1, j, k + 1) or \
                dfs(i - 1, j, k + 1) or \
                dfs(i, j + 1, k + 1) or \
                dfs(i, j - 1, k + 1)
            ):
                return True
            board[i][j] = temp
            return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False