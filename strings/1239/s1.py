# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/solutions/4614192/basic-solution-for-beginners-python-java-c/
class Solution:
    def maxLength(self, arr) -> int:
        # list of all combos
        ls = []
        for i in range(len(arr)):
            flag = 0
            visited = set()
            for j in range(len(arr[i])):
                if arr[i][j] in visited:
                    
                    flag = 1
                    break
                else:
                    visited.add(arr[i][j])
            if flag == 0:
                ls.append(arr[i])
            
        def helper(s, i):
            if i == len(ls):
                return len(s)
            
            not_take = helper(s, i+1)
            flag = 0
            for j in range(len(s)):
                if s[j] in ls[i]:
                    flag = 1
                    break
            take = 0
            if flag == 0:
                take = helper(s + ls[i], i+1)

            return max(take, not_take)
        return helper("", 0)