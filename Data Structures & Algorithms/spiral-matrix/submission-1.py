class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, down, left, right = 0, len(matrix), 0, len(matrix[0])
        res = []
        while left < right and top < down:
            # right
            for col in range(left, right):
                res.append(matrix[top][col])
            top += 1
            for row in range(top, down):
                res.append(matrix[row][right - 1])
            right -= 1
            if not (left < right and top < down):
                break
            for col in range(right - 1, left - 1, -1):
                res.append(matrix[down - 1][col])
            down -= 1
            for row in range(down - 1, top - 1, -1):
                res.append(matrix[row][left])
            left += 1
        return res

                
            
