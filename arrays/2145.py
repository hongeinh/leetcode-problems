# https://leetcode.com/problems/count-the-hidden-sequences
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        max_x = upper
        min_x = lower

        cur = 0
        for difference in differences:
            cur += difference
            # print(cur, end=" ")
            if cur >= 0:
                max_x = min(max_x, upper - cur)
            else:
                min_x = max(min_x, lower - cur)
        
            if max_x < min_x:
                return 0
        # print()
        # print(max_x, min_x)
        return max_x - min_x + 1