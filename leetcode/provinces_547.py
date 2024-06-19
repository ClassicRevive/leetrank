''' Connected components problem '''

# adj list solution
def findCircleNum(isConnected) -> int:
        # convert adj matrix to adj list.
        from collections import defaultdict

        n_nodes = len(isConnected)
        provinces = 0
        graph = defaultdict(list)

        for row in range(len(isConnected)):
            for col in range(row+1, n_nodes):
                if isConnected[row][col] == 1:
                    graph[row].append(col)
                    graph[col].append(row)
        
        print(graph)

        
        # function to traverse province (connected component)
        visited = [False]*n_nodes
        def dfs(node):
            nonlocal visited
            if not visited[node]:
                visited[node] = True
                for next_node in graph[node]:
                    dfs(next_node)
        
        i = 0
        while i < n_nodes:
            if not visited[i]:
                print(f"dfs from {i}")
                dfs(i)
                print(visited)
                provinces += 1
            
            i += 1
        
        return provinces


# adj matrix solution
def findCircleNum_matrix(isConnected) -> int:
        # find neighbors using adj matrix
        from collections import defaultdict

        n_nodes = len(isConnected)
        provinces = 0
        visited = [False]*n_nodes

        def dfs(i, visited):
            if not visited[i]:
                visited[i] = True
                for j in range(n_nodes):
                    if i != j and isConnected[i][j]:
                        dfs(j, visited)
                         
        for i in range(n_nodes):
            if not visited[i]:
                dfs(i, visited)
                provinces += 1

        return provinces

adj_matrix = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(findCircleNum(adj_matrix))
print(findCircleNum_matrix(adj_matrix))