class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        Longest sequence of 1s, given that we can delete k 0's
        
        Solution:
        Dynamic sliding window approach
        '''
        highest = 0
        start = 0
        end = 0

        zeroes = 0
        total=0

        # record the total 0s in the windw
        while end < len(nums):
            if zeroes < k or nums[end] == 1:
                curr = nums[end]
                if curr == 0:
                    zeroes += 1
                total += curr
                end += 1
            else:
                curr = nums[start]
                if curr == 0:
                    zeroes -= 1
                total -= nums[start]
                start += 1

            if total > highest:
                highest = total
        
        return highest + zeroes