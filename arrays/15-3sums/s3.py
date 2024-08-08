class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        nums_occ = {}
        zeros = 0
        for i in nums:
            if i == 0:
                zeros += 1
            elif i in nums_occ:
                nums_occ[i] += 1
            else:
                nums_occ[i] = 1
        if zeros >= 3:
            res.append([0, 0, 0])
        if zeros > 0:
            for i in nums_occ:
                if i > 0:
                    break
                if -i in nums_occ:
                    res.append([i, 0, -i])
        # For num + num = -2 * num
        for i in nums_occ:
            if i > 0:
                break
            elif nums_occ.get(i) > 1 and -2 * i in nums_occ:
                res.append([i, i, -2 * i])
            # elif nums_occ.get(-i/2) and nums_occ.get(-i/2) > 1 and -i/2 in nums_occ:
            #     res.append([i, int(-i/2), int(-i/2)])

        # Other cases:
        for key_low, occ_low in nums_occ.items():
            if key_low > 0:
                break
            for key_high, occ_high in nums_occ.items():
                if key_low >= key_high:
                    continue
                sum = -1 * (key_low + key_high)
                if sum in nums_occ:
                    if sum == key_low and occ_low < 2:
                        continue
                    if sum == key_high and occ_high < 2:
                        continue
                    if sum < key_high: # avoid duplication
                        continue
                    res.append([key_low, key_high, -(key_low + key_high)])
        return res

sol = Solution()
print(sol.threeSum([1,1,-2]))