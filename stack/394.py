# https://leetcode.com/problems/decode-string/description
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        # When traverse s, there are 2 cases
        # not ]: append to stack
        # ]: 
        #   will need to get all characters until meet the first [.
        #   go through string to gather number, until a character is met.
        
        
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                self.extractStack(stack)
        return "".join(stack)

    def extractStack(self, stack):
        cur_str = ""

        # extract duplicate chars:
        # if not [: pop and insert at the front of cur_string
        # if [: just pop and break loop
        while stack:
            c = stack.pop()
            if c == "[":
                break
            cur_str = c + cur_str
        
        # extract the number
        cur_num = ""
        while stack:
            if stack[-1].isdigit():
                cur_num = stack.pop() + cur_num
            else:
                break
        print(cur_str, cur_num)
        new_str = cur_str * int(cur_num)
        stack.append(new_str)