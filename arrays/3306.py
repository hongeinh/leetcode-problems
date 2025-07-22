# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/?envType=daily-question&envId=2025-07-21
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.countAtLeastK(word, k) - self.countAtLeastK(word, k + 1)
    def countAtLeastK(self, word, k): 
        count = 0
        left, right = 0, 0
        vowels = {}
        consonants = 0
        n = len(word)

        while right < n:
            cur = word[right]
            if self.isVowel(cur):
                vowels[cur] = vowels.get(cur, 0) + 1
            else:
                consonants += 1

            while len(vowels.keys()) == 5 and consonants >= k:
                count += n - right
                tmp = word[left]
                if self.isVowel(tmp):
                    vowels[tmp] -= 1
                    if vowels[tmp] == 0:
                        vowels.pop(tmp)
                else:
                    consonants -= 1
                left += 1
            right += 1
        return count 
    def isVowel(self, c):
        return c in ["a", "e", "o", "i", "u"]