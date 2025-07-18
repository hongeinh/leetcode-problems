# https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/?envType=daily-question&envId=2025-07-17
from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = 0
        n = len(dominoes)

        pairs = defaultdict(int)
        for domino in dominoes:
            smaller = domino[0] if domino[0] <= domino[1] else domino[1]
            larger = domino[1] if domino[0] <= domino[1] else domino[0]
            
            pairs[(smaller, larger)] += 1
        print(pairs)
        for _ , count in pairs.items():
            res += count * (count - 1) // 2
        return res
        