class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # suboptimal: TLE
        # optimal: sliding window

        # (1 + 2 + 3)/3 -> (2 + 3 + 4)/3
        from math import mean
        
        start=0
        end=k
        curr = mean(nums[start:end])
        highest = curr
        while end < len(nums):
            curr = curr - nums[start]/k + nums[end]/k
            if curr > highest:
                highest = curr
            
            start += 1
            end += 1
        
        return highest
        