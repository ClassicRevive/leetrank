class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        ''' Longest sub array of ones given that we must delete 1 element
            Basically a special case of max consecutive ones but k=1 and must delete an element
            
            Solution: Dynamic sliding window
            This solution would work even for numbers that aren't 1
        '''
        slow = 0
        fast = 0
        zeroes = 0
        total = 0
        highest = total

        while fast < len(nums):
            if zeroes < 1 or nums[fast]==1:
                if nums[fast] == 0:
                    zeroes += 1
                total += nums[fast]
                fast +=1
            else:
                if nums[slow] == 0:
                    zeroes -= 1
                total -= nums[slow]
                slow += 1
            
            if total > highest:
                highest = total

        if zeroes:
            return highest
        else:
            return highest-1
        
        