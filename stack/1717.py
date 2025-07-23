# https://leetcode.com/problems/maximum-score-from-removing-substrings
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        max_pattern = "ab" if x >= y else "ba"
        min_pattern = "ab" if x < y else "ba"
        first_string = self.erase(s, max_pattern)
        pairs = (len(s) - len(first_string)) // 2
        result = pairs * max(x, y)

        second_string = self.erase(first_string, min_pattern)
        pairs = (len(first_string) - len(second_string)) // 2
        result += pairs * min(x, y)
        return result

    def erase(self, s, pattern) -> int:
        stack = []
        for c in s:
            if c == pattern[1] and stack and stack[-1] == pattern[0]:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)