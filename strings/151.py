# https://leetcode.com/problems/reverse-words-in-a-string
class Solution:
    def reverseWords(self, s: str) -> str:
        words = self.splitWords(s)
        # print(words)
        return " ".join(words[::-1])

    def splitWords(self, s):
        words = []
        cur_word = ""
        for c in s:
            if c != " ":
                cur_word += c
            elif cur_word:
                words.append(cur_word)
                cur_word = ""
        if cur_word:
            words.append(cur_word)
        return words
                