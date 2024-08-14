# https://leetcode.com/problems/car-pooling/
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # get the max number of stops:
        max_stop = 0
        for trip in trips:
            if trip[2] > max_stop:
                max_stop = trip[2]
        
        # initialize num of people per stop
        people_per_stop = [0] * max_stop

        for trip in trips:
            for i in range(trip[1], trip[2]):
                people_per_stop[i] += trip[0]
                if people_per_stop[i] > capacity:
                    return False
        
        return True