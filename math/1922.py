# https://leetcode.com/problems/count-good-numbers/description/?envType=daily-question&envId=2025-04-13
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        self.MOD = 10**9 + 7
        
        def multiply(base, expo):
            result = 1
            multiplier = base
            while expo > 0:
                if expo % 2 == 1:
                    result = result * multiplier % self.MOD
                multiplier = multiplier * multiplier % self.MOD
                expo //=2
            return result
        
        return multiply(5, (n + 1) // 2) * multiply(4, n // 2) % self.MOD
            