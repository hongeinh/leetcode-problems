# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not(grid):
            return -1
        if grid[0][0] or grid[-1][-1]:
            return -1

        rows, cols = len(grid), len(grid[0])
        directions = [[1,1],  [0, 1],  [1, 0], [-1, -1], [-1, 0], [-1, 1], [0, -1], [1, -1]]

        queue = deque([(0, 0, 1)]) # row, col, path length
        found = False
        shortest = float("inf")
        visited = set()
        while queue:
            row, col, path = queue.popleft()
            if row == rows - 1 and col == cols -1:
                return path
            # print(row, col, path)
            for direction in directions:
                new_row, new_col = row + direction[0], col + direction[1]
                if new_row < 0 or new_row == rows:
                    continue
                if new_col < 0 or new_col == cols:
                    continue
                if grid[new_row][new_col]: 
                    continue
                if (new_row, new_col) in visited:
                    continue
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, path + 1))
        return -1