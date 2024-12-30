# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def _insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
    def _getMaxXorBin(self, cur_bin):
        cur = self.root
        answer = ''
        for c in cur_bin:
            required = '1' if c == '0' else '0'
            if required in cur.children:
                answer += '1'
                cur = cur.children[required]
            else:
                answer += '0'
                cur = cur.children[c]
        return answer
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_num = max(nums)
        max_bin_len = len(bin(max_num)) - 2
        
        # Add other nums in binary format into trie
        max_xor = 0
        for num in nums:
            num_bin = bin(num)[2:].zfill(max_bin_len)
            # to make sure all binary have the same length
            self._insert(num_bin)
            cur_xor = self._getMaxXorBin(num_bin)
            max_xor = max(max_xor, int(cur_xor, 2))
        
        return max_xor

class TrieNode:
    def __init__(self):
        self.children = {}