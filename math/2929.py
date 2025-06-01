# https://leetcode.com/problems/distribute-candies-among-children-ii/description/?envType=daily-question&envId=2025-05-31
class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        count = 0
        for i in range(limit + 1):
            possible = min(limit, n - i) - max(0, n - i - limit) + 1 # inclusive so we need +1
            count += max(possible, 0)
        return count
            