# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        start_index = [-1] * 26
        last_index = [-1] * 26
        n = len(s)
        for i in range(n):
            if start_index[ord(s[i]) - 97] == -1:
                start_index[ord(s[i]) - 97] = i
        for i in range(n - 1, -1, -1):
            if last_index[ord(s[i]) - 97] == -1:
                last_index[ord(s[i]) - 97] = i
        # print('start', start_index)
        # print('last', last_index)

        ans = 0
        for i in range(26):
            if start_index[i] == -1 or last_index[i] == -1:
                continue
            unique_between = set()
            for j in range(start_index[i] + 1, last_index[i]):
                unique_between.add(s[j])
            ans += len(unique_between)
    
        return ans