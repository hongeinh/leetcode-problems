
# https://leetcode.com/problems/alternating-groups-ii/description/?envType=daily-question&envId=2025-07-21
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        colors = colors + colors[:k - 1]
        groups = 0
        start = 0
        while start < n:
            prev = colors[start]
            end = start + 1
            count = 1
            # print(start, end, prev)
            while end < n + k - 1 and colors[end] != prev:
                count += 1
                prev = colors[end]
                end += 1
            # print(colors, start, end)
            if count >= k:
                groups += count - k + 1
            start = end
        return groups
