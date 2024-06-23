''' Interesting use of binary search to find peak element. This solution allows for early termination,
but low==high is sufficient for O(logn) solution in general
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def is_peak(A, p):
            return (p == 0 and A[p] > A[p+1]) or (p==len(A)-1 and A[p] > A[p-1]) or \
            (A[p-1] < A[p] and A[p+1] < A[p])
        
        def search(A):
            # binary search for a peak
            # at the point that low = high, we must be at a peak
            low = 0     
            high = len(A) - 1
            while low <= high:
                mid = (high+low)//2

                if low == high or is_peak(A, mid):
                    return mid

                if A[mid] < A[mid+1]:
                    low = mid+1
                else:
                    high = mid

        
        ans = search(nums)
        return ans