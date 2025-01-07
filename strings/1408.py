# https://leetcode.com/problems/string-matching-in-an-array/description/
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        answer = []
        n = len(words)
        for i in range(n - 1):
            for j in range(i + 1, n):
                isSubstring = self.isSubstring(word=words[j], substring=words[i])
                if isSubstring:
                    answer.append(words[i])
                    break
        return answer
    def isSubstring(self, word, substring):
        size = len(substring)
        for i in range(len(word)):
            if word[i:i + size] == substring:
                return True
        return False
       