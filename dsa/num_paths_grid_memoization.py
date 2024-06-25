
def num_of_paths_to_dest(n):
  '''
  Using dfs to find all paths from source to destination given movement constraints.
  Exponential time solution O(Q*2^N). We need to reduce this to O(n^2)
  '''
  global n_paths
  n_paths = 0
  
  def is_valid(pos, n):
    i, j = pos
    return i >= j and 0 <= i < n and 0 <= j < n 
  
  def backtrack(path):
    global n_paths
    
    pos = path[-1]
    if pos == (n-1, n-1):
      n_paths += 1

    dirs = [(1, 0), (0, 1)]
    for i, j in dirs:
      new_i = pos[0] + i
      new_j = pos[1] + j
      
      if is_valid((new_i, new_j), n):
        path.append((new_i, new_j))        
        backtrack(path)
        path.pop()
  
  path = [(0, 0)]
  backtrack(path)
  
  return n_paths


def num_of_paths_to_dest(n):
  '''
  Recursive approach (top-down dynamic programming - memoization)
  
  Note that the path to some position (i, j) is either the path to (i-1, j) then 1 step up, or
  the path to (i, j-1) with 1 step right.
  
  i.e. num_paths_to_square(i, j) = num_paths_to_square(i-1, j) + num_paths_to_square(i, j-1)

  time complexity is O(n^2) since for some i, j we're essentially computing all the coordinates down and to the left of the current,
  and each of those calls is O(1)

  space complexity is also O(n^2). We can reduce the space complexity using an iterative approach, which uses the
  same recurrence relation
  
  '''
  
  # initialise memorization with -1 for each value. memo[i][j] will store the number of paths to position i, j
  memo = [[-1]*n for i in range(n)]
  
  def num_paths_to_square(i, j, memo):
    # base cases
    if i < 0 or j < 0:  # invalid position
      return 0
    elif i < j:  # we require j >= i
      memo[i][j] = 0
    elif memo[i][j] != -1:  # recalling a stored value
      return memo[i][j]
    elif i == 0 and j == 0:
      memo[i][j] = 1
    else:
      memo[i][j] = num_paths_to_square(i-1, j, memo) + num_paths_to_square(i, j-1, memo)
    
    return memo[i][j]
  
  
  return num_paths_to_square(n-1, n-1, memo)


def num_of_paths_to_dest(n):
  '''
  Recursive approach (top-down dynamic programming - memoization)
  
  Note that the path to some position (i, j) is either the path to (i-1, j) then 1 step up, or
  the path to (i, j-1) with 1 step right.
  
  i.e. num_paths_to_square(i, j) = num_paths_to_square(i-1, j) + num_paths_to_square(i, j-1)
  
  '''
  
  # initialise memorization with -1 for each value. memo[i][j] will store the number of paths to position i, j
  memo = [[-1]*n for i in range(n)]
  
  def num_paths_to_square(i, j, memo):
    # base cases
    if i < 0 or j < 0:  # invalid position
      return 0
    elif i < j:  # we require j >= i
      memo[i][j] = 0
    elif memo[i][j] != -1:  # recalling a stored value
      return memo[i][j]
    elif i == 0 and j == 0:
      memo[i][j] = 1
    else:
      memo[i][j] = num_paths_to_square(i-1, j, memo) + num_paths_to_square(i, j-1, memo)
    
    return memo[i][j]
  
  
  return num_paths_to_square(n-1, n-1, memo)


def num_paths_to_dest(n):
  ''' Iterative approach: 
      Same recurrence relation as above, but note that we only need the previous row and the current row to calculate memo[i][j],
      so we don't need to store the whole of memo[i][j] at once.
  
  '''
  
  pass