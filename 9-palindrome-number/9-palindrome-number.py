class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1 or s == s[::-1]:
            return s
        else:
            start, maxlen = 0, 1
            for i in range(1, len(s)):
                print("start: ", start)
                print("max len: ", maxlen)
                print(i - maxlen - 1)
                odd = s[i - maxlen - 1 : i + 1]
                even = s[i - maxlen : i + 1]
                print("odd even: ", odd, even)
                if i - maxlen - 1 >= 0 and odd == odd[::-1]:
                    start = i - maxlen - 1
                    maxlen = maxlen + 2
                    continue
                if even == even[::-1]:
                    start = i - maxlen
                    maxlen = maxlen + 1
            return s[start : maxlen + start]


print(Solution().longestPalindrome("babad"))
