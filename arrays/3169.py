# https://leetcode.com/problems/count-days-without-meetings/

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        merged = []
        for start, end in meetings:
            if not merged:
                merged.append([start, end])
                continue
            prev_start, prev_end = merged[-1]
            if start > prev_end:
                merged.append([start, end])
            elif start <= prev_end:
                merged[-1][1] = max(end, prev_end)
        
        sum_meetings = 0
        for start, end in merged:
            sum_meetings += (end + 1 - start)
        return days - sum_meetings

# line sweep cause memory exceed limit
class LineSweep:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        difference = [0] * (days + 2)
        for start, end in meetings:
            difference[start] += 1
            difference[end + 1] -= 1
        
        cur_meetings = 0
        count = 0
        for i in range(1, days + 1):
            cur_meetings += difference[i]
            if cur_meetings == 0:
                count += 1
        return count