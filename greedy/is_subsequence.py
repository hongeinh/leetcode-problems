# https://leetcode.com/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) > len(t):
            return False
        
        t_start = 0
        s_start = 0

        while t_start < len(t) and s_start < len(s):
            if t[t_start] == s[s_start]:
                s_start += 1
            t_start += 1
        return s_start == len(s)