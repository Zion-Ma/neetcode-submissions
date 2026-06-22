class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        s, e = 0, m * n - 1
        while s <= e:
            mid = s + (e - s) // 2
            x, y = mid // n, mid % n
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                e = mid - 1
            else:
                s = mid + 1
        return False
        