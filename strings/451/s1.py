# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
        sorted_freq = [k*v for k, v in sorted(freq.items(), key=lambda item:item[1], reverse=True)]
        return ''.join(sorted_freq)
    
sol = Solution()
inp = "tree"
print(sol.frequencySort(inp))
