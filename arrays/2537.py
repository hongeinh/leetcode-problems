# https://leetcode.com/problems/count-the-number-of-good-subarrays/
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        same, right = 0, -1
        count = Counter()
        ans = 0

        for left in range(n):
            # print(f"------\nleft = {nums[left]}")
            while same < k and right + 1 < n:
                right += 1
                # print(f"right={right}", end=" ")
                same += count[nums[right]]
                # print(f"same={same}", end=" ")
                count[nums[right]] += 1
                # print(f"count[{nums[right]}]={count[nums[right]]}")

            if same >= k:
                ans += n - right
                # print(f"\nans={ans}")
            count[nums[left]] -= 1
            same -= count[nums[left]]
        return ans

        
