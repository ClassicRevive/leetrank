# iterative solution
def validPath(self, n: int, edges: list, source: int, destination: int) -> bool:
    # dfs from the source. terminate if we reach the destination.
    from collections import defaultdict
    el = defaultdict(list)
    if source == destination:
        return True

    # iterative solution
    # create an edge using the list "edges"
    el = [[] for i in range(n)]
    for a, b in edges:
        el[a].append(b)
        el[b].append(a)
        
    stack = [source]
    visited = [False] * n

    visited[source] = True
    while stack:
        node = stack.pop()
        for edge in el[node]:
            if edge == destination:
                return True
            if not visited[edge]:
                stack.append(edge)
                visited[edge] = True  # as soon as node detected, add it to visited
    
    return visited[destination]


# recursive solution
def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    from collections import defaultdict

    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * n

    def graph_dfs(node):
        if node == destination:
            return True
        
        if not visited[node]:
            visited[node] = True
            for neighbor in graph[node]:
                if graph_dfs(neighbor):  # if statement ensures that if graphdfs returns True from any path, then the output is true.
                    return True

        return False

    return graph_dfs(source)

            



            
            
        