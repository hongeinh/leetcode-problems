# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/description/
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        # 2 ways
        # cut horizontal: col - 1
        # cut vertical: row - 1
        self.MOD = 10**9 + 7
        self.rows, self.cols = len(pizza), len(pizza[0])
        self.pizza = pizza

        self.prefix = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]

        self.memo = {}
        for i in range(self.rows - 1, -1, -1):
            for j in range(self.cols - 1, -1, -1):
                self.prefix[i][j] = (
                    (1 if pizza[i][j] == 'A' else 0) +
                    self.prefix[i + 1][j] +
                    self.prefix[i][j + 1] -
                    self.prefix[i + 1][j + 1]
                )
        return self.helper(0, 0, k - 1)

    def hasApple(self, r1, c1, r2, c2):
        return self.prefix[r1][c1] - self.prefix[r2][c1] - self.prefix[r1][c2] + self.prefix[r2][c2]

    def helper(self, row, col, remaining_cuts):
        # no apple in this section
        if remaining_cuts == 0:
            return 1 if self.hasApple(row, col, self.rows, self.cols) else 0

        if (row, col, remaining_cuts) in self.memo:
            return self.memo[(row, col, remaining_cuts)]
        
        count = 0
        for new_row in range(row + 1, self.rows):
            if self.hasApple(row, col, new_row, self.cols):
                count = (count + self.helper(new_row, col, remaining_cuts - 1)) % self.MOD
        for new_col in range(col + 1, self.cols):
            if self.hasApple(row, col, self.rows, new_col):
                count = (count + self.helper(row, new_col, remaining_cuts - 1)) % self.MOD
        self.memo[(row, col, remaining_cuts)] = count 
        return count


