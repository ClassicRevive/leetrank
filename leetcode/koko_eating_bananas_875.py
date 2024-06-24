''' Brute force solution'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # check how long each pile will take to finish given k eating speed. 
        # if total time > h, then not enough time
        from math import ceil

        low = 1
        high = max(piles)
        while True:
            total_time = 0
            for p in piles:
                total_time += ceil(p/k)
            
            if total_time <= h:
                return k
            
            k += 1


''' Optimisation: binary search '''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # check how long each pile will take to finish given k eating speed. 
        # if total time > h, then not enough time
        from math import ceil

        def is_solution(k):
            nonlocal h
            total_time = 0
            for p in piles:
                total_time += ceil(p/k)

            return total_time <= h    
        
        # binary search for minimum k solution
        low = 1
        high = max(piles)
        while low < high:
            mid = (low+high)//2
            if mid > 1 and is_solution(mid-1):  # there is a solution to the left
                high = mid
            elif not is_solution(mid):
                low = mid+1
            elif is_solution(mid):
                return mid
        
        if low==high and is_solution(low):
            return low
