class Solution:
    def majorityElement(self, nums) -> int:
        count = 0
        element = 0

        for num in nums:
            print("num:", num, ", element:", element, ",count: ", count)
            if count == 0:
                element = num
                count = 1
            elif element == num:
                count += 1
            else:
                count -= 1

        return element

sol = Solution()
print(sol.majorityElement([2,2,1,1,1,2,2,2,3]))