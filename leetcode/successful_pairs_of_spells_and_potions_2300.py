# 
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n_spells = len(spells)
        n_potions = len(potions)
        potions = sorted(potions)
        max_potion = potions[-1]
        pairs = [0]*n_spells
        
        
        def first(A, q):  # binary search for first occurence of q
            low = 0
            high = len(A)-1
            while low <= high:
                mid = (low+high)//2
                
                if (mid == 0 or q > A[mid-1]) and q == A[mid]:
                    return mid
                elif q > A[mid]:
                    low = mid+1
                else:  # if we find the exact threshold, we must linear search for the first occurence of the threshold
                    high = mid-1
            
            if A[low] >= q:
                return low
            
        for i in range(n_spells):
            # for each spell, search for the first successful potion
            spell = spells[i]
            min_p_strength = ceil(success/spell)

            # optimisation: use binary search
            if min_p_strength <= max_potion:
                success_pos = first(potions, min_p_strength)
                pairs[i] += n_potions-success_pos
        
        return pairs
        