# Implementation pattern for max heap (same for min heap)
# Max heap property: For each a node j, the children of node j take values less than or equal to node j's value.



# fix the node at position i such that it conforms to max heap property
def MaxHeapify(A, i, size):
    ''' Worse case O(h) '''
    largest = i
    l = 2*i+1
    r = 2*i+2

    for c in [l, r]:
        if c < size and A[c] > A[largest]:
            largest = c
    
    # base case: node at A[i] is larger than A[l] and A[r]
    if largest == i:
        return
    
    A[i], A[largest] = A[largest], A[i]

    # keep pushing original A[i] downstream
    MaxHeapify(A, largest, size)


# Make the current list into a Max heap by max heap
def BuildMaxHeap(A):
    ''' Intuitive worst case is O(nlogn). Sharp worst case O(n) calculation is a bit weird.
        Consider the number of nodes at each level, and the number of levels and solve for closed form of 
        the sum.'''
    
    i = len(A)//2 - 1
    size=len(A)

    while i >= 0:
        MaxHeapify(A, i, size)
        i -= 1

def HeapSort(A):
    ''' Worst case O(nlogn)'''
    size = len(A)

    # swap largest element into last position
    while size > 1:
        A[0], A[size-1] = A[size-1], A[0]
        size -= 1
        MaxHeapify(A, 0, size)
    


if __name__ == '__main__':
    A = [2, 4, 6, 8, 10, 12, 7, 26]

    BuildMaxHeap(A)
    print(A)
    HeapSort(A)
    print(A)
