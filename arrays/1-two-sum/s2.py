class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            remainder = target - nums[i]
            # print(remainder)
            # print(nums[i+1:])
            # print(remainder in nums[i+1:])
            if remainder in nums[i+1:]:
                return [i, nums[i+1:].index(remainder) + i + 1]

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))