def productExceptSelf(self, nums: List[int]) -> List[int]:
        size=len(nums)
        ans=[0 for i in range(size)]
        zeroes = 0
    
        for i in range(size):
            if nums[i] == 0:
                zeroes +=1
        
        # more than one 0 means all elements in answer array are 0
        if zeroes > 1:
            return ans

        # if we encounter one 0, just compute the product of all the other elements
        if zeroes == 1:
            prod = 1
            for i in range(size):
                if nums[i] == 0:
                    ind=i
                else:
                    prod*=nums[i]
            ans[ind] = prod
            return ans
        
        # if we encounter no 0s, do a rolling division
        fp = 1
        for i in range(size):
            fp *= nums[i]

        for i in range(size):
            ans[i] = fp//nums[i]

        return ans
        