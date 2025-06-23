# https://leetcode.com/problems/sum-of-k-mirror-numbers/description/?envType=daily-question&envId=2025-06-23
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        total = 0
        length = 1
        while n > 0:
            for i in range(length, length * 10):
                if n <= 0:
                    break
                p = self.createPalindrome(i, True)
                if self.isPalindrome(p, k):
                    total += p
                    n -= 1

            for i in range(length, length * 10):
                if n <= 0:
                    break
                p = self.createPalindrome(i, False)
                if self.isPalindrome(p, k):
                    total += p
                    n -= 1
            length *= 10
        return total

    
    def isPalindrome(self, num, base):
        digits = []
        while num > 0:
            digits.append(num % base)
            num //= base
        return digits == digits[::-1]
    
    def createPalindrome(self, num, odd):
        x = num
        if odd:
            x //= 10

        while x > 0:
            num = num * 10 + x % 10
            x //= 10
        return num
    