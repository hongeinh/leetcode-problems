# https://leetcode.com/problems/partition-equal-subset-sum/
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        required = total // 2
        print(required)
        n = len(nums)
        dp = [False] * (required + 1)
        dp[0] = True

        for cur in nums:
            for j in range(required, cur - 1, -1):
                dp[j] = dp[j] or dp[j - cur]
                if dp[required]:
                    break
        return dp[required]
        