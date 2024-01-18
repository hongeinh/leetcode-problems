class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        tmp_x = x
        flipped_values = []
        flipped_value = 0
        while tmp_x != 0:
            quotient, remainder = divmod(tmp_x, 10)
            tmp_x = quotient
            flipped_values.insert(0, remainder)

        for i in range(0, len(flipped_values)):
            flipped_value += flipped_values[i] * pow(10, i)

        print(flipped_value)
        print(x)
        if flipped_value != x:
            return False
        return True
