# https://leetcode.com/problems/increasing-triplet-subsequence/description
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_min = float("inf")
        second_min = float("inf")

        for num in nums:
            if num <= first_min:
                first_min = num
            elif num <= second_min:
                second_min = num
            else:
                # bigger than both
                return True
        return False