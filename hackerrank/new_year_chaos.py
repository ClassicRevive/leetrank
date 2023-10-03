def minimumBribes(q):
    # Write your code here
    
    count = 0
    
    i = 0
    while i < len(q):
        curr = q[i] - (i+1)
        
        # dealing with the case of too many jumps
        if curr > 2:
            print("Too chaotic")
            return
        
        # q[i] - 2 as for any j, if you bribed that j you can end 
        # up at maximum one position behind the original position 
        # of q[i] 
        for j in range(max(0, q[i]-2), i):
            if q[i] < q[j]:  # q[i] was bribed
                count += 1
        
        i += 1

    print(count)
        