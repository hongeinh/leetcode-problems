# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        left_balls, right_balls = 0, 0
        left_moves, right_moves = 0, 0

        for i in range(n):
            answer[i] += left_moves
            left_balls += int(boxes[i])
            left_moves += left_balls

            j = n - 1 - i
            answer[j] += right_moves
            right_balls += int(boxes[j])
            right_moves += right_balls
        return answer