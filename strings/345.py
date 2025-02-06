# https://leetcode.com/problems/reverse-vowels-of-a-string
class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1

        vowels = {'a', 'e', 'u', 'i', 'o', 'A', 'E', 'U', 'I', 'O'}
        chars = list(s)
        while left < right:
            while left < len(s) and s[left] not in vowels:
                left += 1
            while right >= 0 and s[right] not in vowels:
                right -= 1
            if left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        return "".join(chars)
