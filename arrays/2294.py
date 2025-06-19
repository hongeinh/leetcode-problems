# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/description
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        left = 0
        for right in range(n):
            if nums[right] - nums[left] > k:
                count += 1
                left = right
        return count + 1
