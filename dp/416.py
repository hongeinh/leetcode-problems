# https://leetcode.com/problems/partition-equal-subset-sum/
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        n = len(nums)
        dp = [[None for _ in range(total // 2 + 1)] for _ in range(n)]

        def dfs(nums, remaining, cur_sum, target):
            if cur_sum == target:
                return True
            if cur_sum > target:
                return False
            if remaining < 0:
                return False
            if dp[remaining][cur_sum] != None:
                return dp[remaining][cur_sum]
            
            skip = dfs(nums, remaining - 1, cur_sum, target)
            take = dfs(nums, remaining - 1, cur_sum + nums[remaining], target)
            dp[remaining][cur_sum] = skip or take
            return dp[remaining][cur_sum]

        return dfs(nums, n - 1, 0, total // 2)