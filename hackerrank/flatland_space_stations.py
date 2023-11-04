def flatlandSpaceStations(n, c):
    # compute all the distances
    max_dist = 0
    c = sorted(c)
    i = 0
    while i < len(c):
        if i == 0:  # first station, compute distance to left edge
            dist = c[i]
        else:
            dist = (c[i] - c[i-1]) // 2
        
        if dist > max_dist:
            max_dist = dist

        i += 1
    
    # last station, compute distance to right edge
    dist = n - c[len(c)-1] - 1
    if dist > max_dist:
        max_dist = dist
        boundary = True

    return max_dist


print(flatlandSpaceStations(90, [4, 76, 16, 71, 56, 7, 77, 31, 2, 66, 12, 32, 57, 11, 19, 14, 42]))