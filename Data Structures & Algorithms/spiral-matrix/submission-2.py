class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, down, left, right = 0, len(matrix), 0, len(matrix[0])
        result = []
        while left < right and top < down:
            for j in range(left, right):
                result.append(matrix[top][j])
            top += 1
            for i in range(top, down):
                result.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < down):
                break
            for j in range(right - 1, left - 1, -1):
                result.append(matrix[down - 1][j])
            down -= 1
            for i in range(down - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        return result
            
            