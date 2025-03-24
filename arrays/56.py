# https://leetcode.com/problems/merge-intervals/description/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        for start, end in intervals:
            if not result:
                result.append([start, end])
                continue
            prev_start, prev_end = result[-1]
            if start > prev_end:
                result.append([start, end])
            elif start <= prev_end:
                result[-1][1] = max(prev_end, end)
        return result