def countInversions(arr):
    # Write your code here
    
    def mergesort(arr, inversions=0):
        # base case, single-element or empty lists so no more splitting
        
        print("calling mergesort on", arr)
        if len(arr) < 2:
            return 0  
        
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        # recursive split until base case
        inv = mergesort(L) + mergesort(R)
        # merge the lists
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                # when element from right list is added first, this is implicitly len(L)-i swaps!
                arr[k] = R[j]
                inv += (len(L)-i)
                j += 1
            k += 1
        
        # finish the merge
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        
        # from each mergesort the inversion count is returned
        return inv
        
    return mergesort(arr)

def main():
    print(countInversions([2, 3, 1]))
if __name__ == '__main__':
    main()