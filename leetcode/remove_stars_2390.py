class Stack():
            def __init__(self):
                self.items = []
                self.size = 0
            
            def push(self, v):
                self.items.append(v)
                self.size += 1
            
            def pop(self):
                v = "Can't pop from empty stack"
                if self.size > 0:
                    v = self.items.pop()
                return v

            def peek(self):
                if self.size > 0:
                    return self.items[-1]

class Solution:
    def removeStars_suboptimal(self, s: str) -> str:
        ''' This solution is O(n), but manipulates the string s unnecessarily '''
        s = list(s)
        i = 0
        while i < len(s):
            if s[i] == '*':
                s = s[:i-1] + s[i+1:]
                i -= 1
            else:
                i += 1
        
        return "".join(s)

    def removeStars_optimal(self, s:str) -> str:
        ''' Store the non-star elements in a stack. Every time we encounter a star, we pop a character
            from the stack. Still O(n) but much cheaper.
        '''
        chars = Stack()
        for c in s:
            if c != "*":
                chars.push(c)
            else:
                chars.pop()
        
        return "".join(chars.items)

if __name__ == "__main__":
    a = "thisisatesttest****"
    print(Solution().removeStars_suboptimal(a))
    print(Solution().removeStars_optimal(a))