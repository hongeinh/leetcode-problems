# https://leetcode.com/problems/can-place-flowers/description
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)

        for i in range(size):
            if flowerbed[i]:
                continue
            empty_left = (i == 0) or not flowerbed[i - 1]
            empty_right = (i == size - 1) or not flowerbed[i + 1]

            if empty_left and empty_right:
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return n <= 0
        