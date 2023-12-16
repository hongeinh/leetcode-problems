class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s) != len(s)):
            return False
        s_dict = self.toDict(s)
        t_dict = self.toDict(t)
        return self.compareDict(s_dict, t_dict)
        
    def toDict(self, s):
        """
        :type s: str
        :rtype: dictionary
        """
        dict = {}
        for c in s:
            dict[c] = dict.get(c, 0) + 1
        return dict

    def compareDict(self, s, t):
        """
        :type s: dictionary
        :type t: dictionary
        :rtype: bool
        """ 
        return s == t


solution = Solution()
print(solution.isAnagram("rat", "car"))