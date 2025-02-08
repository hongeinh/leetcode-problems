# https://leetcode.com/problems/product-of-array-except-self/description
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        results = [1] * n

        for i in range(1, n):
            results[i] = results[i - 1] * nums[i - 1]
        

        prev = 1
        for i in range(n - 1, -1, -1):
            results[i] = results[i] * prev
            prev *= nums[i]
        return results