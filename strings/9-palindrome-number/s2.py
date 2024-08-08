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
        flipped = 0
        tmp = x
        while(tmp > 0):
            remainder = tmp%10
            tmp = tmp//10
            flipped = flipped * 10 + remainder
        if x == flipped:
            return True
        else: 
            return False
