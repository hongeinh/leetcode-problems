class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        max_len = 0
        i = 0           # ref to tail of the substring
        j = 0           # ref to head of the substring
        indices = {}    # save the indices of each character accountered
        while i < length:
            if s[i] not in indices or indices[s[i]] < j:   # indices[s[i]] < j: means that the currently considered substring does not contain the char s[i]
                if i - j + 1 > max_len:
                    max_len = i - j + 1
            else:
                index = indices[s[i]]
                if j <= index:
                    j = index + 1
            indices[s[i]] = i
            i += 1
        return max_len

