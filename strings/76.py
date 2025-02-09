# https://leetcode.com/problems/minimum-window-substring/description/
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        needed = {}

        for c in t:
            if c not in needed:
                needed[c] = [0, 0]
            needed[c][0] += 1

        left, right = 0, 0
        found = 0
        window = [-1, len(s)]        
        for right in range(len(s)):
            # not the character we care for
            if s[right] not in needed:
                continue
            
            needed[s[right]][1] += 1

            # discovered all what the current char needs
            if needed[s[right]][0] == needed[s[right]][1]:
                found += needed[s[right]][0]
            # hasnt found all chars
            if found < len(t):
                continue

            while True:
                if right - left < window[1] - window[0]:
                    window = [left, right]
                c = s[left]
                if c not in needed:
                    left += 1
                    continue
                needed[c][1] -= 1
                if needed[c][1] < needed[c][0]:
                    found -= needed[c][0]
                    left += 1
                    break
                left += 1
                
            # print(left, right, window)
        if found == len(t) and right - left < window[1] - window[0]:
            window = [left - 1, right]
        return s[window[0]: window[1] + 1] if window != [-1, len(s)] else ""