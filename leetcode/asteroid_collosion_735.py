class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ''' 
            Store left-moving asteroids in a stack, like a contest stack.
            Each right-moving asteroid contests the stack.
        '''
        a = []
        size = 0
        
        i = 0
        while i < len(asteroids):
            asteroid = asteroids[i]
            # right moving asteroid is appended to the stack
            if asteroid > 0:
                a.append(asteroid)
                size += 1

            # left moving asteroid will contest the stack
            tie = False
            if asteroid < 0:
                while size > 0 and -asteroid >= a[-1]:
                    loser = a.pop()
                    size -= 1

                    if -asteroid == loser:
                        tie = True
                        break
                
                # add left asteroid if it defeated the whole stack, or if stack is empty
                if size == 0 and not tie:
                    a.append(asteroid)
                    tie = False
            i += 1
        
        return a



        