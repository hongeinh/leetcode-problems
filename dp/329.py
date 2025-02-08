# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        longest_path = 0
        rows, cols = len(matrix), len(matrix[0])
        memo = [[0 for _ in range(cols)] for _ in range(rows)]
        def dfs(row, col, matrix, prev_val):
            if row < 0 or row >= rows:
                return -1
            if col < 0 or col >= cols:
                return -1
            if matrix[row][col] <= prev_val:
                return -1
            if memo[row][col]:
                return memo[row][col]

            up = dfs(row - 1, col, matrix, matrix[row][col])
            down = dfs(row + 1, col, matrix, matrix[row][col])
            left = dfs(row, col - 1, matrix, matrix[row][col])
            right = dfs(row, col + 1, matrix, matrix[row][col])

            memo[row][col] = max(up, down, left, right) + 1
            return memo[row][col]
        
        for row in range(rows):
            for col in range(cols):
                longest_path = max(longest_path, dfs(row, col, matrix, -1) + 1)
        
        return longest_path