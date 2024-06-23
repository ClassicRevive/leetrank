class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        # pass over array to find the position of rightmost occurence of maximum and leftmost occurence of minimum
        lowest = 0
        highest = 0
        for i in range(len(nums)):
            if nums[i] < nums[lowest]:  # will take first occurence of lowest
                lowest = i
            if nums[i] >= nums[highest]:  # will take last occurence of highest
                highest = i

        # number of swaps for largest is distance between largest and end-of-list position
            
        swaps = 0
        swaps += lowest
        swaps += (len(nums)-1 - highest)

        if lowest > highest:
            swaps -= 1
    
        return swaps
        