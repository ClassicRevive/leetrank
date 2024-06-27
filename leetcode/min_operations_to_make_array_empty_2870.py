class Solution:
    def minOperations(self, nums: List[int]) -> int:
        from collections import defaultdict

        freqs = defaultdict(int)
        for num in nums:
            freqs[str(num)] += 1
        
        ops = 0
        for f in freqs.values():
            # find the minimum number of operations to eliminate frequency f
            curr = f
            if curr == 1:
                return -1

            while curr > 0:
                if curr % 3 == 0:
                    ops += curr//3
                    curr = 0
                elif curr % 3 == 1:
                    curr -= 2
                    ops += 1
                else:
                    curr -= 3
                    ops += 1
        
        return ops
            

