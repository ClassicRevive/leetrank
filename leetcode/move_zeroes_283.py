def moveZeroes_suboptimal(nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        This solution is not in-place
        """
        zeroes = 0
        lst = []
        for num in nums:
            if num != 0:
                lst.append(num)
            else:
                zeroes += 1
        
        for i in range(zeroes):
            lst.append(0)
        
        for i in range(len(nums)):
            nums[i] = lst[i]

def moveZeroes_inplace(nums: list[int]) -> None:
    '''
    If a new found element is not 0, we record it just after the last non-zero element

    cur: finds new elements
    slow: records last non-zero element

    each time we find a non-zero element, we swap it into the slow pointer position
    '''
    last_non_zero_at = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero_at] = nums[i]
            last_non_zero_at += 1
    
    for j in range(last_non_zero_at, len(nums)):
        nums[j] = 0




    

if __name__ == "__main__":
    test1 = [0,1,0,3,12]
    print(test1)
    moveZeroes_suboptimal(test1)
    print(test1)
    print()
    
    test2 = [0,1,0,3,12]
    print(test2)
    moveZeroes_inplace(test2)
    print(test2)
