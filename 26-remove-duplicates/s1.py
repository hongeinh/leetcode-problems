class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        if len(nums) < 2:
            return 1 if nums[0] == nums[1] else 2
            
        while i < len(nums) - 2:
            print(i, i + 1, i + 2, nums)
            if nums[i] == nums[i + 1]:
                if nums[i] == nums[i + 2]:
                    nums.pop(i + 2)
                else: 
                    i += 2
            else: 
                i += 1
        return k

nums = [0,0,1,1,1,1,2,3,3]
sol = Solution()
k = sol.removeDuplicates(nums)
print(k, nums)