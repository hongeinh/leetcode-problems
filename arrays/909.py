# https://leetcode.com/problems/snakes-and-ladders/description/?envType=daily-question&envId=2025-05-31
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        positions = dict()
        r = 0
        while r < n:
            for i in range(n):
                col = i if r % 2 == 0 else n - 1 - i
                positions[i + 1 + n * r] = (n - 1 - r, col)
            r += 1

        queue = [1] # starting point
        distance = [-1] * (n ** 2 + 1) # distance from starting point
        distance[1] = 0
        while queue:
            cur = queue.pop(0)
            row, col = positions[cur]

            for nex in range(cur + 1, min(cur + 6, n**2) + 1):
                nex_row, nex_col = positions[nex]
                destination = board[nex_row][nex_col] if board[nex_row][nex_col] != -1 else nex
                if distance[destination] == -1:
                    distance[destination] = distance[cur] + 1
                    queue.append(destination)
        return distance[n**2]