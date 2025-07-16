# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/description/?envType=daily-question&envId=2025-07-14
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        numsIndex = [(num, i) for i, num in enumerate(nums)]
        numsIndex.sort(reverse=True)
        resultIndex = numsIndex[:k]
        resultIndex.sort(key=lambda x:x[1])
        return [v for (v,_) in resultIndex]
