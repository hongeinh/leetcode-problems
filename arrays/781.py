# https://leetcode.com/problems/rabbits-in-forest/description
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        groups = defaultdict(int)
        for answer in answers:
            groups[answer + 1] += 1

        # print(groups)
        rabbits = 0
        for size, mems in groups.items():
            rabbits += ceil(mems/size) * size
        
        return int(rabbits)