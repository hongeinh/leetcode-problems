# https://leetcode.com/problems/find-the-count-of-good-integers/description
class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        possibleInts = set()
        base = 10 ** ((n - 1) // 2)
        skip = n & 1

        # enumerate the number of palindromes of n digits
        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][skip:]
            palindromicInt = int(s)

            if palindromicInt % k == 0:
                sorted_s = "".join(sorted(s))
                possibleInts.add(sorted_s)
            
        fac = [factorial(i) for i in range(n + 1)]
        ans = 0
        for s in possibleInts:
            count = [0] * 10
            for c in s:
                count[int(c)] += 1
            # calculate permutations and combinations
            total = (n - count[0]) * fac[n - 1]
            for x in count:
                total //= fac[x]
            ans += total
        return ans