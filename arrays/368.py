# https://leetcode.com/problems/largest-divisible-subset/description
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        max_from = n - 1
        lds = {}
        for num in nums:
            lds[num] = [num]
        for i in range(n - 2, -1, -1):
            tmp = []
            for j in range(i + 1, n):
                if nums[j] % nums[i] != 0:
                    continue
                if len(lds[nums[j]]) > len(tmp):
                    tmp = lds[nums[j]]
            lds[nums[i]].extend(tmp)
            if len(lds[nums[i]]) > len(lds[nums[max_from]]):
                max_from = i
        return lds[nums[max_from]]