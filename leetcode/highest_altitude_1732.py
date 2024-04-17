class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # derive altitudes from the gain list and find maximum
        curr = 0
        highest = 0
        for g in gain:
            curr += g
            highest = max(curr, highest)
        
        return highest
        