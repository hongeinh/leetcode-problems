# https://leetcode.com/problems/insert-interval/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0 
        n = len(intervals)
        new_start, new_end = newInterval
        while i < n and new_start > intervals[i][0]:
            i += 1
        while i < n and new_start == intervals[i][0] and new_end >= intervals[i][1]:
            i += 1
        intervals.insert(i, newInterval)
        # print(intervals)
        result = []
        for start, end in intervals:
            if not result:
                result.append([start, end])
                continue
            prev_start, prev_end = result[-1]
            if start > prev_end:
                result.append([start, end])
            else:
                result[-1][1] = max(end, prev_end)
        return result