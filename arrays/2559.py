class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        prefix = [0] * n

        prefix[0] = 1 if self.isValid(words[0]) else 0

        for i in range(1, n):
            vowel = 1 if self.isValid(words[i]) else 0
            prefix[i] = prefix[i - 1] + vowel
        

        # print(prefix)
        answer = []
        for start, end in queries:
            start_isValid = 1 if self.isValid(words[start]) else 0
            answer.append(prefix[end] - prefix[start] + start_isValid)
        return answer

    def isVowel(self, c):
        return c in {'a', 'e', 'i', 'o', 'u'}
    
    def isValid(self, word):
        return self.isVowel(word[0]) and self.isVowel(word[-1])