# https://leetcode.com/problems/find-unique-binary-string
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums.sort()
        for i in range(2**n):
            bin_i = bin(i)[2:]
            bin_i = "0" * (n - len(bin_i)) + bin_i
            if i >= n or bin_i != nums[i]:
                return bin_i
        return None