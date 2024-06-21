import heapq as hq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # simulate hiring using a min heap and candidate constraints.
        n = len(costs)
        total = 0

        left_heap = costs[:candidates]
        right_heap = costs[max(n - candidates, candidates):]  # right heap can be smaller than left, or empty
        hq.heapify(left_heap)
        hq.heapify(right_heap)
        
        next_l = len(left_heap)
        next_r = n - len(right_heap) - 1  
        min_l = hq.heappop(left_heap)
        if right_heap:
            min_r = hq.heappop(right_heap)
        else:
            min_r = float("inf")

        
        for i in range(k):
            if min_l <= min_r:
                total += min_l
                
                if next_l <= next_r:
                    hq.heappush(left_heap, costs[next_l])
                    next_l += 1

                if left_heap:
                    min_l = hq.heappop(left_heap)
                else:  # empty heap
                    min_l  = float("inf")
            else:
                total += min_r

                if next_l <= next_r:
                    hq.heappush(right_heap, costs[next_r])
                    next_r -= 1
                
                if right_heap:
                    min_r = hq.heappop(right_heap)
                else:
                    min_r = float("inf")
        
        return total
        