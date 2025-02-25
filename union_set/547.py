# https://leetcode.com/problems/number-of-provinces/description/
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        numComponents = n

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 0:
                    continue
                if uf.find(i) == uf.find(j):
                    continue
                numComponents -= 1
                uf.union_set(i, j)
        return numComponents


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_set(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        if self.rank[parentX] < self.rank[parentY]:
            self.parent[parentX] = parentY
        elif self.rank[parentX] > self.rank[parentY]:
            self.parent[parentY] = parentX
        else:
            self.parent[parentY] = parentX
            self.rank[parentX] += 1