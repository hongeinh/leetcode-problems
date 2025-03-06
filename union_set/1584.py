# https://leetcode.com/problems/min-cost-to-connect-all-points/description/
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = []
        n = len(points)
        ds = DisjointSet(n)

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                # print(points[i] , "->", points[j], "=", distance)
                distances.append((distance, i, j))
        edges = 0   # number of edges <= n - 1
        weight = 0
        distances.sort()
        # print(distances)
        for distance, i, j in distances:
            # loop
            if ds.find(i) == ds.find(j):
                continue
            ds.union(i, j)
            edges += 1
            weight += distance

            if edges == n - 1:
                break

        return weight

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parentx = self.find(x)
        parenty = self.find(y)

        if parentx == parenty:
            return
        if self.rank[parentx] < self.rank[parenty]:
            self.parent[parentx] = parenty
        elif self.rank[parentx] > self.rank[parenty]:
            self.parent[parenty] = parentx
        else:
            self.parent[parenty] = parentx
            self.rank[parentx] += 1