class Solution:
    def productExceptSelf(self, nums):
        result = []
        for i in range(nums):
            product = 1
            for j in range(nums):
                if i != j:
                    product *= nums[j]
            result.append(product)

        return result
        