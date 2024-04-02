class Solution:
    def productExceptSelf(self, nums):
        result = [1] * len(nums)
        prefixProduct = 1
        suffixProduct = 1
        for i in range(len(nums)):
            result[i] *= prefixProduct
            prefixProduct *= nums[i]
        for j in range(len(nums) - 1, -1, -1):
            result[j] *= suffixProduct
            suffixProduct *= nums[j]

        return result