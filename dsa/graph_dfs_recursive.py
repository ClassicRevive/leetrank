''' This is a good example of the recursive graph dfs pattern '''

def dfs(curr):
    global visited
    if not visited[curr]:
        # adjust the body of recursive call to fit the objective
        visited[curr] = True
        for node in adjlist[curr]:
            dfs(node)

def solve(adjlist) -> bool:
    global visited

    n_nodes = len(adjlist)
    visited = [False]*n_nodes
    
    dfs(0)
    return visited

# graph as an adjacency list  representation
adjlist = [[1, 2], [0, 2], [0, 1]]

print(solve(adjlist))