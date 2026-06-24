class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, w = len(board), len(board[0]), len(word)
        def traverse(i: int, j: int, k: int) -> bool:
            if k == w: return True
            if (
                not m > i >= 0 or\
                not n > j >= 0 or\
                k >= w or\
                board[i][j] != word[k]
            ): return False
            temp = board[i][j]
            board[i][j] = "."
            result = (
                traverse(i + 1, j, k + 1) or\
                traverse(i - 1, j, k + 1) or\
                traverse(i, j + 1, k + 1) or\
                traverse(i, j - 1, k + 1)
            )
            board[i][j] = temp
            return result
        
        for i in range(m):
            for j in range(n):
                if traverse(i, j, 0):
                    return True
        return False