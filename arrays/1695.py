# https://leetcode.com/problems/maximum-erasure-value/description
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        uniques = set()
        left, right = 0, 0
        n = len(nums)
        longest = 0
        score = 0
        total = sum(nums)
        while right < n:
            cur = nums[right]
            # print("cur", cur)
            if cur in uniques: 
                while left < n and cur in uniques:
                    score -= nums[left]
                    uniques.remove(nums[left])
                    # print("remove", nums[left], "score", score)
                    left += 1
            uniques.add(cur)
            score += cur
            longest = max(longest, score)
            # print("add", cur, "score", score)

            right += 1
        return longest