# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/
from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        rounds = 0
        frequencies = Counter(tasks)
        
        for key, val in frequencies.items():
            if val < 2:
                return -1
            elif val % 3 == 0:
                rounds += val // 3
            else:
                rounds += val // 3 + 1
        return rounds