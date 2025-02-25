# https://leetcode.com/problems/all-paths-from-source-to-target/
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.n = len(graph)
        self.results = []
        self.explore(0, graph, [], [False] * self.n)
        return self.results
    
    def explore(self, source, graph, cur_path, visited):
        if source == self.n - 1:
            new_cur = cur_path.copy()
            new_cur.append(self.n - 1)
            self.results.append(new_cur)
            return
        if visited[source]:
            return
        cur_path.append(source)
        visited[source] = True
        for node in graph[source]:
            self.explore(node, graph, cur_path, visited)
        cur_path.pop()
        visited[source] = False
        
