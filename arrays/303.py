# https://leetcode.com/problems/range-sum-query-immutable/description/
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.prefix = [0] * self.n

        prev = 0
        for i in range(self.n):
            self.prefix[i] = prev
            prev += nums[i]
        
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right] + self.nums[right] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)