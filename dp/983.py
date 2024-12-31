# https://leetcode.com/problems/minimum-cost-for-tickets/description/
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        max_day = max(days)
        dp = [0] * (max_day + 1)

        travel_days = set(days)
        for day in range(1, max_day + 1):
            if day not in travel_days:
                dp[day] = dp[day - 1]
                continue
            # price if buy one day pass
            min_price = dp[day - 1] + costs[0]
            if day - 7 >= 0:
                min_price = min(min_price, dp[day - 7] + costs[1])
            else:
                min_price = min(min_price, costs[1])

                
            if day - 30 >= 0:
                min_price = min(min_price, dp[day - 30] + costs[2])
            else:
                min_price = min(min_price, costs[2])
            dp[day] = min_price
            # print(day, dp[day])
        # for i in range(max_day + 1):
        #     print(i, dp[i], i in travel_days)
        return dp[-1]