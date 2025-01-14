# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        common = [0] * n

        appeared = set()
        cur_common = 0
        for i in range(n):
            if A[i] == B[i]:
                cur_common += 1
                common[i] = cur_common
                continue
            if A[i] in appeared:
                cur_common += 1
            else:
                appeared.add(A[i])
            if B[i] in appeared:
                cur_common += 1
            else:
                appeared.add(B[i])
            common[i] = cur_common

        return common
        