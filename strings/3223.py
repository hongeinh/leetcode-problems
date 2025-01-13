# https://leetcode.com/problems/minimum-length-of-string-after-operations/
from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        frequencies = Counter(s)
        
        removed = 0
        for c, freq in frequencies.items():
            if freq >= 3:
                while freq > 2:
                    freq -= 2
                    removed += 2

        return len(s) - removed   
        