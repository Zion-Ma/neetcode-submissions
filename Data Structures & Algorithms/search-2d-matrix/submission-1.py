class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = matrix.__len__(), matrix[0].__len__()
        s, e = 0 , m * n - 1
        while s <= e:
            mid = s + (e - s) // 2
            row, col = mid // n, mid % n
            val = matrix[row][col]
            if val > target:
                e = mid - 1
            elif val < target:
                s = mid + 1
            else:
                return True
        return False