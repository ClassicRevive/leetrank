''' Both methods work exclusively for a directed acyclic graph'''
''' backtracking method '''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        n = len(graph)
        results = []

        def backtrack(node, path):
            if node == n-1:
                results.append(list(path))
            
            for next_node in graph[node]:
                path.append(next_node)
                backtrack(next_node, path)
                path.pop()

        path = [0]
        backtrack(0, path)

        return results


'''Dynamic programming: 
Paths from current node = curr_node + paths from next node
'''
from functools import lru_cache
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph)-1
        
        @lru_cache(maxsize=None)
        def all_paths_to_target(node):
            if node == target:
                return [[target]]
            
            # results built during recursive calls
            results = []
            for next_node in graph[node]:
                for path in all_paths_to_target(next_node):
                    results.append([node] + path)

            return results

        results = all_paths_to_target(0)
        return results
    
#   dp = [][]
#   for i from 0 to n-1:
#     for j from 0 to n-1:
#       db[i][j] = -1
      
#   backtrack(i, j, memo):
#     if(i < 0 OR j < 0):
#        return 0
#     elif (i > j):
#       memo[i][j] = 0
#     elif memo[i][j] != -1
#       return memo[i][j]
#     elif i == 0 and j ==0:
#       memo[i][j] = 1
#     else:
#       memo[i][j] = backtrack(i, j-1, memo) + backtrack(i-1, j, memo)
      


        
                    