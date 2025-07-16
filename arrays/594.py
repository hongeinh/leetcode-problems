# https://leetcode.com/problems/longest-harmonious-subsequence/?envType=daily-question&envId=2025-07-14
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        frequencies = defaultdict(int)

        for num in nums:
            frequencies[num] += 1
        
        longest = 0
        for k, v in frequencies.items():
            if (k + 1) in frequencies:
                longest = max(longest, v + frequencies[k + 1])
            if (k - 1) in frequencies:
                longest = max(longest, v + frequencies[k - 1])
        return longest