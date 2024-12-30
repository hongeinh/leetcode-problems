class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        
        count = 0
        num_rows = len(grid)
        nums_col = len(grid[0])
        # Use DFS to explore the depth of each island cluster
        stack = []
        
        for r in range(num_rows):
            for c in range(nums_col):
                if grid[r][c] == 1:
                    self.findIsland(grid, r, c)
                    count += 1
        return count
    

    def findIsland(self, grid, current_row, current_col):
        # base case ? when the surroundings of the current position is all water and edge and already visited nodes
        if (current_row < 0 or current_row > len(grid) or 
            current_col < 0 or current_col > len(grid[0]) or 
            grid[current_row][current_col]):
            return
        grid[current_row][current_col] = 0
        self.findIsland(grid, current_row + 1, current_col) # down
        self.findIsland(grid, current_row -1, current_col)  # up
        self.findIsland(grid, current_row, current_col + 1) # right
        self.findIsland(grid, current_row, current_col + 1)  # left
