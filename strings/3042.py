# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if len(words[i]) > len(words[j]):
                    continue
                if self.isPrefixSuffix(words[j], words[i]):
                    count += 1
        return count

    def isPrefixSuffix(self, word, pattern):
        return self.isPrefix(word, pattern) and self.isSuffix(word, pattern)
    def isPrefix(self, word, pattern):
        return word[:len(pattern)] == pattern

    def isSuffix(self, word, pattern):
        return word[len(word) - len(pattern):] == pattern
        