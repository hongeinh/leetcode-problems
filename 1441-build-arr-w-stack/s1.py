class Solution:
    def __init__(self) -> None:
        self.commands = []
        
        
    def buildArray(self, target, n):
        start = 0
        end = len(target) - 1
        
        for i in range(1, n + 1):
            self.push()
            if target[start] != i:
                self.pop()
            else:
                start += 1
    
    def push(self):
        self.commands.append("Push")
    

    def pop(self):
        self.commands.append("Pop")
        
        
        
sol = Solution()
# sol.buildArray([1, 3], 3)
sol.buildArray([1, 2, 3], 3)
print(sol.commands)