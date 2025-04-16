# https://leetcode.com/problems/count-number-of-homogenous-substrings/description/
class Solution:
    def countHomogenous(self, s: str) -> int:
        n = len(s)
        ans = 0
        MOD = 10**9 + 7
        left, right = 0, 0
        while left < n:
            while right < n and s[left] == s[right]:
                right += 1
            
            length = right - left
            ans += length * (length + 1) // 2
            # print(f"length={length}, left={left}, right={right}, ans={ans}")
            ans %= MOD
            left = right
            
        return ans % MOD