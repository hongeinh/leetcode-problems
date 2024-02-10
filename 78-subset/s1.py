

class Solution:
    def subsets(self, nums):
        if len(nums) == 0:
            return [[]]

        nums = sorted(nums)
        result = [[], nums]
        memo = {}
        memo[self.join_arr(nums)] = nums
        for i in range(len(nums)):
            self.omit_item(nums, i, result, memo)
        return result


    def omit_item(self, base_arr, rm_index, result, memo): 
        if len(base_arr) == 0:
            return
        new_arr = base_arr.copy()
        new_arr.pop(rm_index)
        if(memo.get(self.join_arr(new_arr)) or len(new_arr) == 0):
            return
        result.append(new_arr)
        memo[self.join_arr(new_arr)] = new_arr
        for i in range(len(new_arr)):
            self.omit_item(new_arr, i, result, memo)

    def join_arr(self, arr):
        return ",".join(str(i) for i in arr)

    
nums = [1, 2, 3, 4]
sol = Solution()
print(sol.subsets(nums))
            