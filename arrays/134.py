# https://leetcode.com/problems/gas-station/description
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain = 0
        cur_gain = 0
        answer = 0
        stations = len(gas)
        for station in range(stations):
            total_gain += gas[station] - cost[station]
            cur_gain += gas[station] - cost[station]

            if cur_gain < 0:
                cur_gain = 0
                answer = station + 1
        return answer if total_gain >= 0 else -1