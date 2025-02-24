# https://leetcode.com/problems/most-profitable-path-in-a-tree/description/
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        self.max_profit = float("-inf")
        self.n = len(edges) + 1
        self.adjacency_matrix = defaultdict(list)

        for node1, node2 in edges:
            self.adjacency_matrix[node1].append(node2)
            self.adjacency_matrix[node2].append(node1)
        self.bobPath = {}
        self.visited = [False] * self.n

        self.findBobPath(bob, 0)
        print(self.bobPath)
        queue = [(0, 0, 0)] # alice, time, profit
        self.visited = [False] * self.n
        while queue:
            node, time, profit = queue.pop(0)

            # bob doesnt go thru this node
            # or reach this node later than alice
            if node not in self.bobPath or time < self.bobPath[node]:
                profit += amount[node]
            # bob go thru this node at the same time
            elif time == self.bobPath[node]:
                profit += amount[node] // 2
            if len(self.adjacency_matrix[node]) == 1 and node != 0:
                self.max_profit = max(self.max_profit, profit)
                continue

            for nex_node in self.adjacency_matrix[node]:
                if self.visited[nex_node]:
                    continue
                queue.append((nex_node, time + 1, profit))
            self.visited[node] = True
        return self.max_profit

    def findBobPath(self, source, time):
        self.bobPath[source] = time
        self.visited[source] = True
        if source == 0:
            return True
        for node in self.adjacency_matrix[source]:
            if self.visited[node]:
                continue
            if self.findBobPath(node, time + 1):
                return True
        del self.bobPath[source]
        return False
