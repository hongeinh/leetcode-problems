# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.happy_strings = []
        self.generateString(0, "", n, [0], k)

        if len(self.happy_strings) < k:
            return ""
        return self.happy_strings[k - 1]

    def generateString(self, index, cur_string, n , count, k):
        if index == n:
            self.happy_strings.append(cur_string)
            return 
            
        for c in ["a", "b", "c"]:
            if cur_string and c == cur_string[-1]:
                continue    
            self.generateString(index + 1, cur_string + c, n, count, k)
            
        