class Solution:
    def maxScore(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]**2
        max_factor = self.calcMaxFactor(nums)
        for i in range(len(nums)):
            print("--Remove", nums[i])
            factor = self.calcMaxFactor(nums[:i] + nums[i + 1:])
            max_factor = max(max_factor, factor)
        return max_factor
    def calcMaxFactor(self, nums):
        n = len(nums)
        lcms = [1] * (n) 
        gcds = [1] * (n)
        gcds[0] = nums[0]
        lcms[0] = nums[0]
        prev_lcm = nums[0]
        for i in range(1, n):
            gcds[i] = self.gcd(gcds[i-1], nums[i])
            lcms[i] = self.lcm(prev_lcm, nums[i], gcds[i])
            prev_lcm = lcms[i]
        print(gcds)
        print(lcms)
        return gcds[-1] * lcms[-1]
        

    def gcd(self, a, b): 
        # base case
        if a == 0 or b == 0:
            return max(a, b)
        if a == b:
            return a
        if a % b == 0:
            return b
        if b % a == 0:
            return a
        
        while b:
            if b > a:
                a, b = b, a
            if a % b:
                return b
            a = a - b
        return 1

    def lcm(self, a, b, gcd):
        # base case
        if a % b == 0:
            return a
        if b % a == 0:
            return b
        return int(a * b / gcd)