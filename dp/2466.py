# https://leetcode.com/problems/count-ways-to-build-good-strings/description/
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[zero] += 1
        dp[one] += 1

        ways = 0
        for i in range(1, high + 1):
            if i - zero >= 0:
                dp[i] += dp[i - zero]
            if i - one >= 0:
                dp[i] += dp[i - one]
            if low <= i <= high:
                ways = (ways + dp[i]) % 1000000007
        # print(dp)
        return int(ways)