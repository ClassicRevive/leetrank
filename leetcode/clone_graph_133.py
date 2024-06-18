"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.visited = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # base case: no nodes
        if not node:
            return

        # base case: visited node
        if node in self.visited:
            return self.visited[node]
        
        # add new cloned node
        cloned_node = Node(node.val)
        self.visited[node] = cloned_node

        # add neighbors
        for next_node in node.neighbors:
            cloned_node.neighbors.append(self.cloneGraph(next_node))
        
        return cloned_node
        
        
        