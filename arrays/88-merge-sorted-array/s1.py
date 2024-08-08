class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) == 0:
            return

        i, j = 0, 0
        while i < m + n and j < n:
            if nums1[i] == 0 and i >= m:
                nums1[i] = nums2[j]
                i += 1
                j += 1
            elif (nums1[i] <= nums2[j]):
                i += 1
            elif nums1[i] > nums2[j]:
                print(nums2[j])
                nums1.insert(i, nums2[j])
                del nums1[m + n]
                print(nums1)
                i += 1 
                j += 1
        
nums1 = [1,2,3,0,0,0]; m = 3; nums2 = [2,5,6]; n = 3

sol = Solution()
sol.merge(nums1, m, nums2, n)
print(nums1)




            

