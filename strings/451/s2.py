from collections import defaultdict, Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)
        bucket = defaultdict()

        result = []
        for char, freq in frequency.items():
            bucket(freq).append(char)

        for i in range(len(s), 0, -1):
            for c in bucket[i]:
                result.append(c*i)
        
        return result
    
sol = Solution()
inp = "tree"
print(sol.frequencySort(inp))