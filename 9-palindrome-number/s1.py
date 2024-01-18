class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        digits = []
        flipped = 0
        while(x > 0):
            remainder = x%10
            digits.append(remainder)
            x = x//10
            flipped = flipped * 10 + remainder
        size = len(digits)
        for i in range(size/2):
            if digits[i] != digits[size - 1 - i]:
                return False
        return True
