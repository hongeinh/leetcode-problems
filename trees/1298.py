# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/?envType=daily-question&envId=2025-06-03
class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        n = len(status)
        closed_boxes = set()
        total = 0

        queue = []
        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)
            else:
                closed_boxes.add(box)
        
        while queue:
            box = queue.pop(0)
            total += candies[box]

            # open new boxes:
            for next_box in keys[box]:
                status[next_box] = 1
                if next_box in closed_boxes:
                    closed_boxes.remove(next_box)
                    queue.append(next_box)

            for next_box in containedBoxes[box]:
                if status[next_box] == 0:
                    closed_boxes.add(next_box)
                else:
                    queue.append(next_box)
        return total
