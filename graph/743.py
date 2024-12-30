# https://leetcode.com/problems/network-delay-time/description/
import math
class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        min = 0
        # initializa a priority queue to remember which node has been used
        priority_queue = self.convertTimes(times)    # convert time to extract what neighboring nodes of each node are
        distances = []      # keep tracks of distances from the start node
        visited = [0] * n

        # need to add something into priority_queue here

        # main logic
        while priority_queue:
            curr = priority_queue.pop() # curr = (node, distance from start)
            visited

    
    def convertTimes(self, times):
        pass


    def findMaxDistance(self, distances):
        max = 0
        max_index = 0
        for i, distance in enumerate(distances):
            if distance > max:
                max = distance
                max_index

        