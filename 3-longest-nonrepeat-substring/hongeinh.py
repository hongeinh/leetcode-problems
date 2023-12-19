class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if (length) == 0:
            return
        max_str = 1
        tmp_str = max_str
        i = 0
        j = 0
        while i < length:
            print(i, j, tmp_str, max_str)
            if s[i] in tmp_str:
                if len(tmp_str) > max_str:
                    max_str = len(tmp_str)
                i = i + tmp_str.index(s[i])
                j = 1
                # i = tmp_str.index(s[i]) + 1
                tmp_str = s[i]
            else:
                tmp_str += s[i]
            i += 1
        return max_str

sol = Solution()
print(sol.lengthOfLongestSubstring('abcabcbb'))
