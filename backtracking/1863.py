# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        self.subsets = []
        self.n = len(nums)
        xor_results = {}
        self.backtrack(0, [], nums)
        # print(self.subsets)
        total = 0
        for subset in self.subsets:
            total += self.getXor(subset)
        return total

    def getXor(self, subset):
        result = 0
        for num in subset:
            result ^= num
        return result
        
    def backtrack(self, start, cur_subset, nums):
        self.subsets.append(cur_subset.copy())
        for i in range(start, self.n):
            cur_subset.append(nums[i])
            self.backtrack(i + 1, cur_subset, nums)
            cur_subset.pop()