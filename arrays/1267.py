# https://leetcode.com/problems/count-servers-that-communicate/
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        row_count, col_count = [0] * rows, [0] * cols 
        for row in range(rows):
            row_count[row] = sum(grid[row])
        
        for col in range(cols):
            count = 0
            for row in range(rows):
                count += grid[row][col]
            col_count[col] = count
        
        connected = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue
                if row_count[row] == 0 or col_count[col] == 0:
                    continue
                if row_count[row] == 1 and col_count[col] == 1:
                    continue
                connected += 1
        return connected