# nasty weighted graph division problem. Could probably use BFS to be quicker, but DFS with backtracking is accepted.
# Finds a single path from source to target, and multiplies the weights sequentially. 

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build graph from equations
        # if a/b = n1, then a = b*n1 and b = a*(1/n1)
        # so this is a directed, weighted graph between nodes a and b
        # if we want to evaulate a/c, we need to start at node a and traverse to c, multiplying by the weights.

        from collections import defaultdict
        graph = defaultdict(list)
        
        # build the weighted graph
        for i, (a, b) in enumerate(equations):
            graph[a].append([b, values[i]])
            graph[b].append([a, 1/values[i]])


        def backtrack(var, target, visited, path):
            # find path to the target using backtracking algorithm
            if var == target:
                return True

            if not visited[var]:
                visited[var] = True

                for next_var in graph[var]:
                    var = next_var[0]
                    path.append(var)
                    
                    # propagate truth value up recursion tree - if the path is found
                    if backtrack(var, target, visited, path):
                        return True
                    path.pop()

            return False
        
        answers = []
        for source, target in queries:
            visited = defaultdict(bool)
            path = [source]
            
            # if the path is found, calculate the answer
            if (source in )backtrack(source, target, visited, path):
                prod = 1
                i = 0
                while i < len(path)-1:
                    # find next node in path in the graph
                    for node, weight in graph[path[i]]:
                        if node == path[i+1]:
                            prod *= weight    
                    i += 1
                
                answers.append(prod)
            else:
                answers.append(-1)
        
        return answers


        