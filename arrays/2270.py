# https://leetcode.com/problems/word-search-ii/
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * n
        suffix_sum = [0] * n

        cur_sum = 0
        for i in range(n):
            cur_sum += nums[i]
            prefix_sum[i] = cur_sum
        
        cur_sum = 0
        for i in range(n - 1, -1, -1):
            cur_sum += nums[i]
            suffix_sum[i] = cur_sum
        
        count = 0
        for i in range(n - 1):
            if prefix_sum[i] >= suffix_sum[i + 1]:
                count += 1
        return count