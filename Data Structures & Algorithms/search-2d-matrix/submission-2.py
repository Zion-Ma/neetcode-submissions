class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1
        while start <= end:
            mid = start + (end - start) // 2
            row, col = mid // n, mid % n
            val = matrix[row][col]
            if val > target:
                end = mid - 1
            elif val < target:
                start = mid + 1
            else:
                return True
        return False
