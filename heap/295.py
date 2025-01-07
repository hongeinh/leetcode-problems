# https://leetcode.com/problems/find-median-from-data-stream/description/
class MedianFinder:

    def __init__(self):
        self.max_heap = [] # max heap, lower half
        self.min_heap = [] # min_heap, higher half


    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        max_top = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, -max_top)

        if len(self.max_heap) < len(self.min_heap):
            min_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_top)

    def findMedian(self) -> float:
        # print("max", self.max_heap)
        # print("min", self.min_heap)
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()