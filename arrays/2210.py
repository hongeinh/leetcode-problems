# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        uniques = []
        prev = None
        for num in nums:
            if num != prev:
                uniques.append(num)
                prev = num
        
        n = len(uniques)
        prefix = [False] * n
        suffix = [False] * n # True = taller, False = smaller
        for i in range(1, n):
            if uniques[i - 1] < uniques[i]:
                prefix[i] = True
        for i in range(n - 2, -1, -1):
            if uniques[i + 1] < uniques[i]:
                suffix[i] = True
        count = 0
        for i in range(1, n - 1):
            if prefix[i] == suffix[i]:
                count += 1
        return count  