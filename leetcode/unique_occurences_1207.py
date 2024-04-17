class Solution:
    def uniqueOccurrences_nlogn(self, arr: List[int]) -> bool:
        ''' This is O(n*logn) due to the sorting '''
        from collections import defaultdict

        # store frequencies
        counts = defaultdict(int)
        for i in range(len(arr)):
            counts[arr[i]] += 1

        # sort frequencies and iterate through
        counts = sorted(counts.values())
        prev = 0
        for i in range(len(counts)):
            if counts[i] == prev:
                return False
            prev = counts[i]
        
        return True
    
    def uniqueOccurrences_on(self, arr):
        ''' This is O(n) '''
        from collections import defaultdict

        # store frequencies
        counts = defaultdict(int)
        for i in range(len(arr)):
            counts[arr[i]] += 1

        # sort frequencies and iterate through
        counts = sorted(counts.values())
        prev = 0
        for i in range(len(counts)):
            if counts[i] == prev:
                return False
            prev = counts[i]
        
        return True
    