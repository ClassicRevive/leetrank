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



        
                    