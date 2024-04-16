def increasingTriplet(self, nums: List[int]) -> bool:
    '''
    Record first and second minimum pointers
    '''
    n = len(nums)
    # Longest increasing subsequence (DP) special case.

    first = float("inf")
    second = float("inf")

    # in a case where the first pointer is ahead, we know that there exists a number behind the second pointer that
    # is less than it.
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    
    return False
    
    


