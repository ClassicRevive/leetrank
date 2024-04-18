class Solution:
    def decodeString(self, s: str) -> str:
        '''
            Since we need to do the operations from the innermost to the outermost, use stack.
            The solution is sort of like a DFS algorithm on a list, since we go to the innermost
            operation and work backwords (LIFO).
        '''
        class Stack():
            def __init__(self):
                self.items = []
                self.size = 0
            
            def push(self, v):
                self.items.append(v)
                self.size += 1
            
            def pop(self):
                v = self.items.pop()
                self.size -= 1
                return v
            
            def peek(self):
                if stack.size > 0:
                    return self.items[-1]
                return "empty"

        
        stack = Stack()
        for i in range(len(s)):
            if s[i] != "]":  # keep pushing till "]"
                stack.push(s[i])
            else:
                to_decode = []
                while stack.peek() != "[":
                    to_decode.append(stack.pop())
                
                stack.pop()  # get rid of open bracket
                k = ""
                while "0" <= stack.peek() and stack.peek() <= "9":
                    k = stack.pop() + k
                k = int(k)

                to_decode = to_decode*k

                for i in range(len(to_decode)):
                    stack.push(to_decode[-1-i])
            
        return "".join(stack.items)


                
            
            


           


            
            
        