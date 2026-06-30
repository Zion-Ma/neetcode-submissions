class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowZero = False
        m, n = len(matrix), len(matrix[0])
        for j in range(n):
            if matrix[0][j] == 0:
                rowZero = True
                break
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for i in range(m):
                matrix[i][0] = 0
        if rowZero:
            for j in range(n):
                matrix[0][j] = 0
        