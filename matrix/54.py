# https://leetcode.com/problems/spiral-matrix/description/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        row, col = 0, 0
        result = []
        while len(result) < len(matrix) * len(matrix[0]):
            # move right
            for col in range(left, right + 1):
                result.append(matrix[row][col])
            
            # move down
            for row in range(top + 1, bottom + 1):
                result.append(matrix[row][col])

            if top != bottom:
                # move left
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[row][col])

            if left != right:
                # move up
                for row in range(bottom - 1, top, -1):
                    result.append(matrix[row][col])
            
            bottom -= 1
            right -= 1
            top += 1
            left += 1
        return result