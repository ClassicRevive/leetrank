''' If we sort the array, we can solve this using two pointers.
    We can also use hashmaps or brute force to solve it
'''

class Solution:
    def maxOperations_suboptimal(self, nums: list[int], k: int) -> int:
        ops = 0
        used = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i not in used and j not in used and nums[i] + nums[j] == k:
                    ops += 1
                    used.append(i)
                    used.append(j)

        return ops
    
    def maxOperations_hashmap(self, nums: list[int], k: int) -> int:
        from collections import defaultdict
        ops = 0
        
        # store counts of each number
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        # for each number n, how many occurences of k-n are there?
        for num, c in counts.items():
            if num == k/2:
                ops += c//2
                counts[num] -= c//2
            elif k-num in counts:  # 2 numbers make up k
                sums = min(counts[num], counts[k-num])
                ops += sums
                counts[num] -= sums
                counts[k-num] -= sums

        return ops
        

if __name__ == "__main__":
    s = Solution()
    print(s.maxOperations_hashmap([3,5,1,5], 2))
    