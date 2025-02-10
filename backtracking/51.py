# https://leetcode.com/problems/n-queens/description
QUEEN = "Q"
SPACE = "."

class Solution:
    def backtrack(self, row, n, positions):
        # violates row, col, or diagonal
        if row == n:
            self.ways.append(positions.copy())
            return

        for col in range(n):
            if self.isValidPosition(row, col, positions):
                positions.append(col)
                self.backtrack(row + 1, n, positions)
                positions.pop()


    def isValidPosition(self, row, col, positions):
        for r, c in enumerate(positions):
            if c == col or abs(row - r) == abs(col - c):
                return False
        return True


    def fillBoard(self, queens, n):
        # Final result
        board = []
        for row in range(n):
            line = [SPACE] * n
            line[queens[row]] = QUEEN
            board.append("".join(line))
        return board

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ways = []
        self.backtrack(0, n, [])
        
        return [self.fillBoard(way, n) for way in self.ways]