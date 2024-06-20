class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # dfs from node 0. if the node is not pointing towards the origin, then add 1 to reorder count.
        # since the graph takes a tree structure, and there is only one way to reach each city, this is sufficient
        from collections import defaultdict
        reorders = 0
        visited = [False] * n
        directed = defaultdict(list)
        undirected = defaultdict(list)

        for a, b in connections:
            undirected[a].append(b)
            directed[a].append(b)
            undirected[b].append(a)
        
        def dfs_reorder(node, visited):
            nonlocal reorders

            if not visited[node]:
                visited[node] = True
                for next_node in undirected[node]:
                    if not visited[next_node] and node not in directed[next_node]:
                        reorders += 1
                    
                    dfs_reorder(next_node, visited)


        dfs_reorder(0, visited)
        return reorders