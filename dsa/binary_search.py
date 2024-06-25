
# iterative, equivalent to bisect_left behaviour
def bsearch(arr, q):
    n = len(arr)
    low = 0
    high = n-1

    while low < high:
        mid = (low+high)//2
        if q == arr[mid]:
            return mid
        elif q < arr[mid]:
            high = mid  # with the -1 here, the high can cross over the low, but if the value is present it will be returned
        else:
            low = mid+1
    
    if arr[low] != q:
        print(f"{q} not found, would be in position where {arr[low]} is")
    if high == low:
        return low
    print(f"low: {low}, high: {high}")

# recursive
def bsearch_rec(arr, q, low, high):
    mid = (low+high)//2
    # base case: not found
    if low > high:
        print(f"{q} not found")
        return

    # base case
    if arr[mid]==q:
        return mid
    elif q > arr[mid]:
        return bsearch_rec(arr, q, mid+1, high)
    else:
        return bsearch_rec(arr, q, low, mid-1)


# first occurrence binary search
def first(arr, q):
    low = 0
    high = len(arr)-q
    while low <= high:
        mid = (low+high)//2
        # leftmost condition
        if (mid == 0 or q > arr[mid-1]) and arr[mid] == q:
            return mid
        elif q > arr[mid]:
            low = mid+1
        else:
            high = mid-1
    
    # didn't find occurence. This behaviour may be tweaked depending on the problem
    return -1


if __name__ == '__main__':
    arr = [3, 4, 5, 6, 7, 19, 22]
    ans_it = bsearch(arr, 22)
    ans_rec = bsearch_rec(arr, 22, 0, len(arr)-1)
    print(f"Position = {ans_it}, item = {arr[ans_it]}")
    print(f"Position = {ans_rec}, item = {arr[ans_rec]}")
    print(f"Solutions match: {ans_it==ans_rec}")

    print("Not found example:")
    bsearch(arr, 8)
    bsearch_rec(arr, 8, 0, len(arr)-1)


    # print("First occurrence example:")
    # arr = [3, 4, 5, 5, 5, 6, 8]
    # ans_it= bsearch(arr, 5)
    # ans_first = first(arr, 5)
    # print(f"Position = {ans_it}, item = {arr[ans_it]}")
    # print(f"Position = {ans_first}, item = {arr[ans_first]}")
