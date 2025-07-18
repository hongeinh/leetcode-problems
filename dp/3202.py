# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/description/?envType=daily-question&envId=2025-07-17
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod_nums = [num % k for num in nums]
    
        longest = 0
        for i in range(k): 
            dp = [0] * k
            for j in range(n):
                mod = mod_nums[j]
                pos = (i - mod + k) % k # to prevent negative number
                dp[mod] = dp[pos] + 1
                longest = max(longest, dp[mod])
        return longest