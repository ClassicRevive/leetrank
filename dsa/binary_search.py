
# iterative
def bsearch(a, q):
    n = len(a)
    low = 0
    high = n-1
    

    while low < high:
        mid = (low+high)//2
        if q == a[mid]:
            return mid
        elif q < a[mid]:
            high = mid
        else:
            low = mid+1
    
    return print(f"{q} not found")


# recursive
def bsearch_rec(a, q, low, high):
    mid = (low+high)//2
    # base case: not found
    if low >= high:
        print(f"{q} not found")
        return

    # base ca
    if a[mid]==q:
        return mid
    elif q > a[mid]:
        return bsearch_rec(a, q, mid+1, high)
    else:
        return bsearch_rec(a, q, low, mid)


if __name__ == '__main__':
    a = [3, 4, 5, 6, 7, 19, 22]
    ans_it = bsearch(a, 7)
    ans_rec = bsearch_rec(a, 7, 0, len(a)-1)
    print(f"Position = {ans_it}, item = {a[ans_it]}")
    print(f"Position = {ans_rec}, item = {a[ans_rec]}")
    print(f"Solutions match: {ans_it==ans_rec}")

    bsearch(a, 8)
    bsearch_rec(a, 8, 0, len(a)-1)
