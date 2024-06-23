# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.path_length = 0
            
        def dfs(node, parent, steps):
            ''' Recursive calls down the tree in both directions, keeping track of the number of zigzag steps on the current path
                if the zig zag steps exceed the current maximum, update the maximum (maximum is like a global variable) '''
            if node:
                self.path_length = max(steps, self.path_length)

                if parent is None:
                    dfs(node.right, "left", steps+1)
                    dfs(node.left, "right", steps+1)
                if parent == "right":
                    dfs(node.right, "left", steps + 1)
                    dfs(node.left, "right", 1)
                elif parent == "left":
                    dfs(node.left, "right", steps + 1)
                    dfs(node.right, "left", 1)

        dfs(root, None, 0)
        return self.path_length
        
        

            


            
        