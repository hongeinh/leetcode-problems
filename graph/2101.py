# https://leetcode.com/problems/detonate-the-maximum-bombs/
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        distances = [[0 for _ in range(n)] for _ in range(n)]

        # calc distance from 1 bomb to all others
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1, _ = bombs[i]
                x2, y2, _ = bombs[j]
                distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
                distance = sqrt(distance)
                distances[i][j] = distance
                distances[j][i] = distance
            
        # get the list of bombs this current bomb can affect
        detonatable = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                _, _, r1 = bombs[i]
                _, _, r2 = bombs[j]
                if distances[i][j] <= r1:
                    detonatable[i].append(j)
                if distances[i][j] <= r2:
                    detonatable[j].append(i)
        max_detonatable = 1

        # traverse to see max detonatable boms
        for i in range(n):
            visited = [False] * n
            count = self.dfs(i, detonatable, visited)
            max_detonatable = max(max_detonatable, count)
        return max_detonatable


    def dfs(self, bomb, detonatable, visited):
        count = 1
        visited[bomb] = True
        for other in detonatable.get(bomb, []):
            if visited[other]:
                continue
            count += self.dfs(other, detonatable, visited)
        return count
