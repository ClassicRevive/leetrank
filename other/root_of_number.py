def root(x, n):
  '''
  nth root of x
  
  looking for number a such that a multiplied by itself n times gives x
  
  so if we search for a in the range 0 to x, we will find a number satisfying condition
  above using binary search
  
  low is 0
  high is x
  
  check mid
  
  
  Example:
  x = 9
  n = 2
  
  we start with low=0
  high = 4.5
  
  mid = 2.25
  if mid ** n is in the range 8.99, 9.001, then return mid
  '''
  
  # x = 4.5
  # n = 2
  
  def is_solution(a, n, target):
    ans = a
    for i in range(n-1):
      ans *= a
    
    if ans < target-0.001:
      return 1
    if ans > target+0.001:
      return -1
    else:
      return 0

  low = 0
  high = x
  while low < high:
    mid = (low+high)/2
    
    if is_solution(mid, n, x) == -1:
      high = mid
    elif is_solution(mid, n, x) == 1:
      low = mid+0.00001
    else:
      return mid
