class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        ''' 
        Sub-optimal solution: Simulating the senate using greedy algorithm on the array
        Here we have to make removal operations on the list that are O(n)
        '''
        
        from collections import defaultdict
        
        # helper function to ban the specified party, start at the next index
        # return looparound indicator
        def ban(start, to_ban):
            i = start
            looparound = False
            while True:
                if i == 0:
                    looparound = True
                if senate[i] == to_ban:
                    senate.pop(i)
                    break

                i = (i + 1) % len(senate)

            return looparound
        
        senate = list(senate)
        r_count = senate.count('R')
        d_count = len(senate) - r_count

        # It is now the turn of the Senator at this index
        turn = 0    
        # keep going until there's a winner
        while r_count > 0 and d_count > 0:
            if senate[turn] == 'R':
                loop = ban((turn+1) % len(senate), 'D')
                d_count -= 1
            else:
                loop = ban((turn+1) % len(senate), 'R')
                r_count -= 1
            
            if loop:
                turn -= 1
            
            turn = (turn+1)%len(senate)
        
        if r_count > 0:
            return "Radiant"
        else:
            return "Dire"
        