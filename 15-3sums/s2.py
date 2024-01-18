class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        size = len(nums)
        results = []
        exist_i = set()
        for i in range(0, size - 2):
            if nums[i] in exist_i:
                continue
            exist_j = set()
            for j in range(i + 1, size - 1):
                if nums[i] + nums[j] == 0 and abs(nums[i]) != 0 :
                    break
                if nums[j] in exist_j:
                    continue
                else: 
                    exist_k = set()
                    for k in range(j + 1, size):
                        if nums[k] in exist_k:
                            continue
                        if nums[i] + nums[j] + nums[k] == 0:
                            print(i, j, k, nums[i], nums[j], nums[k])
                            results.append([nums[i], nums[j], nums[k]])
                            break
                        exist_k.add(nums[k])

                    exist_j.add(nums[j])
            exist_i.add(nums[i])
        return list(results)

sol = Solution()
# print(sol.threeSum([-1,0,1,2,-1,-4]))
print(sol.threeSum([0,0,0]))
