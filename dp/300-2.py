# https://leetcode.com/problems/longest-increasing-subsequence/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]

        for num in nums[1:]:
            i = self.findIndex(sub, num)
            # print(sub, num, i)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)
    
    def findIndex(self, sub, num):
        lo, hi = 0, len(sub) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if sub[mid] < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo