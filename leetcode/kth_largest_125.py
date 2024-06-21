
# We can get down to O(n*logk) using a heap with max size k.
# So in this case, we push each number to a minimum heap. If size exceeds k, then we pop.
# The final state of the heap will contain the k largest elements.
import heapq

# much faster solution
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use a minimum heap of size k
        import heapq as hq
        
        heap = []
        for num in nums:
            hq.heappush(heap, num)
            if len(heap) > k:
                hq.heappop(heap)
        
        return heap[0]
            




# original slow solution using a max heap with unbounded size.
# The worst case runtime here is O(nlog(n))
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Rearrange list into a max heap and extract elements until kth element
        # assuming k << n, worst case runtime is O(n + k*log(n)) = O(n)

        def MaxHeapify(A, i, size):
            largest = i
            l = 2*i+1
            r = 2*i+2

            for c in [l, r]:
                if c < size and A[c] > A[largest]:
                    largest = c
            
            # base case: largest didn't change
            if largest == i:
                return
            
            
            # recursive call
            A[i], A[largest] = A[largest], A[i]
            MaxHeapify(A, largest, size)
        
        def BuildMaxHeap(A):
            size = len(A)

            i = len(A)//2 - 1
            while i >= 0:
                MaxHeapify(A, i, size)
                i -= 1
        
        def kth_largest(A, k):
            size = len(A)
            
            for i in range(k):
                A[0], A[size-1] = A[size-1], A[0]
                size -= 1
                MaxHeapify(A, 0, size)
            
            return A[-k]
        
        BuildMaxHeap(nums)
        return kth_largest(nums, k)

